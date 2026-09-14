#!/usr/bin/env python3
import os
import re
import glob

def clean_filename(name):
    # Remove illegal filename characters
    cleaned = re.sub(r'[\\/*?:\"<>|]', '', name).strip()
    cleaned = re.sub(r'\s+', ' ', cleaned)
    # Truncate if overly long
    if len(cleaned) > 120:
        cleaned = cleaned[:120].strip()
    return cleaned

def extract_clipping_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Section
    section = ""
    m_sec = re.search(r'розділ:\s*\"?([^\n\r\"]+)\"?', content)
    if m_sec:
        section = m_sec.group(1).strip()

    # Segment
    segment = ""
    m_seg = re.search(r'сегмент:\s*\"?([^\n\r\"]+)\"?', content)
    if m_seg:
        segment = m_seg.group(1).strip()

    # Heading 1
    h1 = ""
    m_h1 = re.search(r'^#\s+(.+)$', content, re.M)
    if m_h1:
        h1 = m_h1.group(1).strip()

    # Fix User Safety classification artifact
    if "User Safety" in segment or not segment:
        # Search for first numbered heading or line in text (e.g. 11. ... or 86. ...)
        m_num = re.search(r'(?:^|\n)(\d+\.\s+[^\n\.\!]+[\.\!]?)', content)
        if m_num:
            segment = m_num.group(1).strip()
        elif h1 and "User Safety" not in h1:
            segment = h1
        else:
            base = os.path.basename(file_path)[:-3]
            parts = base.split('_', 2)
            segment = parts[-1].replace('_', ' ') if len(parts) > 2 else base

    if "User Safety" in h1 or not h1:
        h1 = segment

    # Extract related concepts
    related = []
    rel_match = re.search(r'## Пов\'язані концепти(.*?)(?:$|\n##)', content, re.S)
    if rel_match:
        related = re.findall(r'\[\[(.*?)\]\]', rel_match.group(1))

    # Extract body text without frontmatter and ## Пов'язані концепти
    body = content
    if body.startswith('---'):
        parts = body.split('---', 2)
        if len(parts) >= 3:
            body = parts[2].strip()

    # Remove trailing ## Пов'язані концепти from body
    body = re.sub(r'## Пов\'язані концепти.*$', '', body, flags=re.S).strip()

    return {
        "section": section,
        "segment": segment,
        "h1": h1,
        "related": related,
        "body": body,
        "raw": content
    }

def determine_tags_and_parent(folder, section, segment):
    tags = []
    parents = []
    group = "concepts"

    if folder == "making_json_segments":
        tags = ["право", "судова_аргументація", "скаліа_гарнер"]
        parents.append("Скаліа (Antonin Scalia)")
        parents.append("Making Your Case (Посібник)")
        if "I." in section or "Загальні принципи" in section:
            parents.append("Загальні_принципи_судової_аргументації")
        elif "II." in section or "правовий аналіз" in section.lower():
            parents.append("Правовий_аналіз_та_стандарти_доказування")
        elif "III." in section or "процесуальні документи" in section.lower() or "брифінг" in section.lower():
            parents.append("Письмова_аргументація")
        elif "IV." in section or "усні виступи" in section.lower():
            parents.append("Усна_аргументація")
    elif folder == "attaking_json-segments":
        if "помилк" in section.lower() or "fallac" in section.lower() or "глава 5" in section.lower() or "глава 6" in section.lower() or "глава 7" in section.lower() or "глава 8" in section.lower():
            tags = ["логіка", "логічні_помилки", "деймер"]
            parents.append("Логічні помилки")
            group = "fallacies"
        elif "кодекс" in section.lower() or "поведінк" in section.lower():
            tags = ["логіка", "етика_дискусії", "деймер"]
            parents.append("Кодекс_інтелектуальної_поведінки")
        else:
            tags = ["логіка", "критерії_аргументу", "деймер"]
            parents.append("П_ять_критеріїв_хорошого_аргументу")
    elif folder == "logica_json_segments":
        tags = ["логіка", "підручник_логіки", "щербина"]
        parents.append("Логіка (як наука)")
        if "поняття" in section.lower():
            parents.append("Поняття")
        elif "судження" in section.lower():
            parents.append("Судження")
        elif "умовивід" in section.lower():
            parents.append("Умовивід")
        elif "закон" in section.lower():
            parents.append("Закони логіки")
        elif "доведення" in section.lower():
            parents.append("Доведення")
    elif folder == "scherbina_json_segments":
        tags = ["право", "юридична_аргументація", "щербина"]
        parents.append("Юридична аргументація")
        parents.append("Олена Щербина")
    elif folder == "theory_json_segments":
        tags = ["право", "теорія_права", "макормік"]
        parents.append("Макормік (Neil MacCormick)")
        parents.append("Юридичний позитивізм")

    return tags, parents, group

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    vault_dir = os.path.join(base_dir, "logicaobsidiant")
    clippings_dir = os.path.join(vault_dir, "Clippings")
    concepts_dir = os.path.join(vault_dir, "wiki", "concepts")
    index_path = os.path.join(vault_dir, "index.md")
    log_path = os.path.join(vault_dir, "log.md")

    os.makedirs(concepts_dir, exist_ok=True)

    existing_concepts = {}
    for f in os.listdir(concepts_dir):
        if f.endswith('.md'):
            existing_concepts[f[:-3].lower()] = f[:-3]

    created_count = 0
    skipped_count = 0
    new_concept_entries = []

    # Iterate over all clippings
    for root, dirs, files in os.walk(clippings_dir):
        folder = os.path.basename(root)
        for file in sorted(files):
            if not file.endswith('.md'):
                continue

            file_path = os.path.join(root, file)
            rel_source = os.path.relpath(file_path, vault_dir)
            meta = extract_clipping_metadata(file_path)

            title = clean_filename(meta["segment"])
            if not title:
                title = clean_filename(meta["h1"])
            if not title:
                title = clean_filename(file[:-3])

            # Check if this concept already exists in concepts_dir
            if title.lower() in existing_concepts:
                # Already exists
                skipped_count += 1
                continue

            tags, parents, group = determine_tags_and_parent(folder, meta["section"], meta["segment"])

            # Collect wikilinks to include in related
            all_related = list(set(meta["related"] + parents))

            # Build YAML frontmatter
            frontmatter_lines = [
                "---",
                "type: concept",
                f"group: {group}",
                "tags:"
            ]
            for t in tags:
                frontmatter_lines.append(f"  - {t}")
            frontmatter_lines.extend([
                "created: 2026-09-14",
                "updated: 2026-09-14",
                "sources:",
                f'  - "[[{rel_source}]]"',
                "---",
                ""
            ])

            # Build body
            content_lines = frontmatter_lines
            content_lines.append(f"# {title}\n")
            if meta["section"]:
                content_lines.append(f"**Розділ:** {meta['section']}\n")

            # Clean body: strip initial duplicate H1 if present
            clean_body = meta["body"]
            clean_body = re.sub(r'^#\s+[^\n]+\n*', '', clean_body).strip()
            # Remove any metadata notes already captured
            clean_body = re.sub(r'^\*\*Розділ:\*\*.*?\n*', '', clean_body).strip()

            content_lines.append(clean_body)
            content_lines.append("\n\n---")
            content_lines.append("## Зв'язки та пов'язані концепти")
            if all_related:
                for r in sorted(all_related):
                    content_lines.append(f"- [[{r}]]")
            content_lines.append(f"- Першоджерело: [[{rel_source}|{file[:-3]}]]\n")

            # Write file
            target_path = os.path.join(concepts_dir, f"{title}.md")
            with open(target_path, 'w', encoding='utf-8') as cf:
                cf.write("\n".join(content_lines))

            existing_concepts[title.lower()] = title
            created_count += 1
            new_concept_entries.append({
                "title": title,
                "folder": folder,
                "section": meta["section"]
            })

    print(f"Compilation finished: {created_count} concepts created, {skipped_count} existing concepts retained.")

    # Append to index.md if new concepts were created
    if new_concept_entries:
        with open(index_path, 'a', encoding='utf-8') as idx:
            idx.write("\n\n---\n## Скомпільовані розділи та правила з першоджерел (Clippings)\n\n")
            # Group by folder
            by_folder = {}
            for entry in new_concept_entries:
                by_folder.setdefault(entry["folder"], []).append(entry)

            folder_titles = {
                "making_json_segments": "Making Your Case (Правила судової аргументації Скаліа та Гарнера)",
                "attaking_json-segments": "Attacking Faulty Reasoning (Логічні помилки та кодекс Деймера)",
                "logica_json_segments": "Підручник логіки (В. Щербина)",
                "scherbina_json_segments": "Юридична аргументація (О. Щербина)",
                "theory_json_segments": "Теорія права (Н. Макормік)"
            }

            for fld, entries in by_folder.items():
                sec_title = folder_titles.get(fld, fld)
                idx.write(f"\n### {sec_title}\n\n")
                for e in sorted(entries, key=lambda x: x['title']):
                    idx.write(f"- [{e['title']}](wiki/concepts/{e['title']}.md)\n")

        # Append to log.md
        with open(log_path, 'a', encoding='utf-8') as lg:
            lg.write(f"\n\n## [2026-09-14] ingest | Повна компіляція першоджерел Clippings у wiki/concepts\n\n")
            lg.write(f"- **Дія**: Скомпільовано {created_count} розділів та сегментів із каталогу `Clippings/` у повноцінні статті `wiki/concepts/`.\n")
            lg.write(f"- **Джерела**: 5 бібліотек першоджерел (`attaking_json-segments`, `making_json_segments`, `logica_json_segments`, `scherbina_json_segments`, `theory_json_segments`).\n")
            lg.write(f"- **Результат**: Створено фронтматтери, виправлено артефакти розмітки, налаштовано зв'язки з батьківськими концептами та оновлено `index.md`.\n")

if __name__ == "__main__":
    main()
