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
    elif folder == "douglas_json_segments":
        tags = ["логіка", "неформальна_логіка", "теорія_аргументації", "волтон"]
        parents.append("Дуглас Волтон (Douglas Walton)")
        parents.append("Неформальна логіка (Informal Logic)")
        sec_lower = section.lower()
        seg_lower = segment.lower()

        if "глава 1" in sec_lower:
            tags.extend(["діалог", "критична_дискусія"])
            parents.append("Типи аргументативного діалогу")
            parents.append("Діалог переконання")
            if "хиб" in seg_lower or "опудал" in seg_lower:
                group = "fallacies"
        elif "глава 2" in sec_lower:
            tags.extend(["інтерогативна_логіка", "запитання_відповіді"])
            parents.append("Логіка запитань і відповідей (Інтерогативна логіка)")
            if "незнанн" in seg_lower or "передрішенн" in seg_lower or "складні запитання" in seg_lower:
                group = "fallacies"
                parents.append("Логічні помилки")
        elif "глава 3" in sec_lower:
            tags.extend(["релевантність", "критика_аргументації"])
            parents.append("Релевантність аргументації")
            if "оселедець" in seg_lower or "нерелевантн" in seg_lower:
                group = "fallacies"
                parents.append("Логічні помилки")
        elif "глава 4" in sec_lower:
            tags.extend(["емоційні_апеляції", "логічні_помилки"])
            parents.append("Апеляції до емоцій")
            parents.append("Логічні помилки")
            group = "fallacies"
        elif "глава 5" in sec_lower:
            tags.extend(["валідність", "дедукція", "дефезибільні_міркування"])
            parents.append("Валідність аргументу")
            parents.append("Дефезибільні міркування")
            if "невалідн" in seg_lower or "помилк" in seg_lower or "поспішний висновок" in seg_lower:
                group = "fallacies"
        elif "глава 6" in sec_lower:
            tags.extend(["ad_hominem", "особиста_атака", "критичні_запитання"])
            parents.append("Атаки на особистість (Ad Hominem)")
            parents.append("Критичні запитання")
            group = "fallacies"
        elif "глава 7" in sec_lower:
            tags.extend(["ad_verecundiam", "думка_експерта", "схеми_аргументації"])
            parents.append("Апеляція до авторитету (Ad Verecundiam)")
            parents.append("Схеми аргументації (Argumentation Schemes)")
            if "помилк" in seg_lower:
                group = "fallacies"
        elif "глава 8" in sec_lower:
            tags.extend(["індукція", "каузальність", "post_hoc", "статистика"])
            parents.append("Каузальні помилки")
            parents.append("Індуктивні міркування")
            group = "fallacies"
        elif "глава 9" in sec_lower:
            tags.extend(["природна_мова", "аналогія", "слизький_схил", "еквівокація"])
            parents.append("Аргумент за аналогією")
            parents.append("Слизький схил")
            if "еквівокац" in seg_lower or "амфібол" in seg_lower or "слизьк" in seg_lower:
                group = "fallacies"
        elif "вступні" in sec_lower:
            tags.extend(["вступ", "методологія"])
    elif folder == "rulebook_json_segments":
        tags = ["логіка", "теорія_аргументації", "практична_аргументація", "вестон"]
        parents.append("Ентоні Вестон (Anthony Weston)")
        parents.append("Посібник з аргументації (A Rulebook for Arguments)")
        sec_lower = section.lower()
        seg_lower = segment.lower()

        if "вступні матеріали" in sec_lower:
            tags.extend(["вступ", "бібліографія"])
        elif "вступ" in sec_lower:
            tags.extend(["вступ", "сенс_аргументації", "дослідження"])
            parents.append("Аргументація")
        elif "розділ i." in sec_lower or "короткі аргументи" in sec_lower:
            tags.extend(["короткі_аргументи", "засновки_висновок", "структура_аргументу"])
            parents.append("Засновки та висновки")
            parents.append("Структура аргументу")
        elif "розділ ii." in sec_lower or "на прикладах" in sec_lower:
            tags.extend(["індукція", "приклади", "репрезентативність", "контрприклади"])
            parents.append("Аргументи на прикладах (Узагальнення)")
            parents.append("Недедуктивні умовиводи")
        elif "розділ iii." in sec_lower or "за аналогією" in sec_lower:
            tags.extend(["аналогія", "подібність"])
            parents.append("Аргумент за аналогією")
            parents.append("Аналогія в юридичній аргументації")
        elif "розділ iv." in sec_lower or "від авторитету" in sec_lower:
            tags.extend(["авторитет", "джерела", "ad_verecundiam"])
            parents.append("Апеляція до авторитету (Ad Verecundiam)")
            parents.append("Схеми аргументації (Argumentation Schemes)")
        elif "розділ v." in sec_lower or "про причини" in sec_lower:
            tags.extend(["каузальність", "причинність", "кореляція"])
            parents.append("Каузальні помилки")
            parents.append("Причинно-наслідкові аргументи")
        elif "розділ vi." in sec_lower or "дедуктивні аргументи" in sec_lower:
            tags.extend(["дедукція", "силогізми", "modus_ponens", "modus_tollens", "reductio_ad_absurdum"])
            parents.append("Дедуктивні умовиводи")
            parents.append("Валідні аргументи")
            parents.append("Дедуктивне виправдання")
        elif "розділ vii." in sec_lower or "розгорнуті аргументи" in sec_lower:
            tags.extend(["розгорнуті_аргументи", "дослідження_теми", "заперечення"])
            parents.append("Стратегія та побудова аргументу")
            parents.append("Побудова аргументації")
        elif "розділ viii." in sec_lower or "аргументативні есе" in sec_lower:
            tags.extend(["аргументативне_есе", "письмова_аргументація", "структура_есе"])
            parents.append("Аргументативне есе")
            parents.append("Письмова_аргументація")
        elif "розділ ix." in sec_lower or "усні аргументи" in sec_lower:
            tags.extend(["усні_виступи", "ораторське_мистецтво", "публічний_виступ"])
            parents.append("Усна_аргументація")
            parents.append("Стратегія_усного_виступу")
        elif "розділ x." in sec_lower or "публічні дебати" in sec_lower:
            tags.extend(["публічні_дебати", "етика_дискусії", "спільна_мова"])
            parents.append("Кодекс інтелектуальної поведінки")
            parents.append("Діалог переконання")
        elif "додаток i." in sec_lower or "типові логічні помилки" in sec_lower:
            tags.extend(["логічні_помилки", "софізми", "fallacies"])
            parents.append("Логічні помилки")
            group = "fallacies"
        elif "додаток ii." in sec_lower or "визначення" in sec_lower:
            tags.extend(["визначення", "дефініції", "семантика"])
            parents.append("Логічні операції з поняттями")
            parents.append("Семантична інтерпретація в праві")
        elif "джерела" in sec_lower:
            tags.extend(["бібліографія", "джерела"])
            parents.append("Література")

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
            if not file.endswith('.md') or file.startswith('_'):
                continue

            file_path = os.path.join(root, file)
            rel_source = os.path.relpath(file_path, vault_dir)
            meta = extract_clipping_metadata(file_path)

            title = clean_filename(meta["segment"])
            if not title:
                title = clean_filename(meta["h1"])
            if not title:
                title = clean_filename(file[:-3])

            if folder == "douglas_json_segments":
                if title == "Передмова":
                    title = "Передмова (Дуглас Волтон)"
                elif title == "Титул, вихідні дані та анотація":
                    title = "Титул, вихідні дані та анотація (Дуглас Волтон)"
                elif title == "Зміст книги":
                    title = "Зміст книги (Дуглас Волтон)"
                elif title == "Подяки":
                    title = "Подяки (Дуглас Волтон)"

            if folder == "rulebook_json_segments":
                if "Титул, вихідні дані та анотація" in title:
                    title = "Титул, вихідні дані та анотація (Ентоні Вестон - A Rulebook for Arguments)"
                elif "Зміст книги" in title:
                    title = "Зміст книги (Ентоні Вестон - A Rulebook for Arguments)"
                elif "Передмова" in title:
                    title = "Передмова (Ентоні Вестон - A Rulebook for Arguments)"
                elif "Примітка до п'ятого видання" in title:
                    title = "Примітка до п'ятого видання (Ентоні Вестон)"
                elif "Джерела та література" in title:
                    title = "Джерела та література (Ентоні Вестон - A Rulebook for Arguments)"

            # Check if this concept already exists in concepts_dir
            if title.lower() in existing_concepts:
                # Already exists
                skipped_count += 1
                continue

            tags, parents, group = determine_tags_and_parent(folder, meta["section"], meta["segment"])

            # Collect wikilinks to include in related
            all_related = list(set(meta["related"] + parents))

            if folder == "rulebook_json_segments":
                item_created = "2026-09-18"
            elif folder == "douglas_json_segments":
                item_created = "2026-09-17"
            else:
                item_created = "2026-09-14"
            item_updated = item_created

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
                f"created: {item_created}",
                f"updated: {item_updated}",
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

    # Update index.md if new concepts were created
    if new_concept_entries:
        # Check raw sources in index.md
        with open(index_path, 'r', encoding='utf-8') as idx_r:
            idx_content = idx_r.read()

        if "douglas_json_segments" not in idx_content:
            idx_content = idx_content.replace(
                "- [[Clippings/theory_json_segments/|theory_json_segments]] — Теоретичні основи теорії аргументації.\n",
                "- [[Clippings/theory_json_segments/|theory_json_segments]] — Теоретичні основи теорії аргументації.\n- [[Clippings/douglas_json_segments/|douglas_json_segments]] — Дуглас Волтон: Неформальна логіка (прагматичний підхід до діалогу, критичні запитання, схеми аргументації).\n"
            )

        if "rulebook_json_segments" not in idx_content:
            idx_content = idx_content.replace(
                "- [[Clippings/douglas_json_segments/|douglas_json_segments]] — Дуглас Волтон: Неформальна логіка (прагматичний підхід до діалогу, критичні запитання, схеми аргументації).\n",
                "- [[Clippings/douglas_json_segments/|douglas_json_segments]] — Дуглас Волтон: Неформальна логіка (прагматичний підхід до діалогу, критичні запитання, схеми аргументації).\n- [[Clippings/rulebook_json_segments/|rulebook_json_segments]] — Ентоні Вестон: Посібник з аргументації (50 практичних правил побудови, дедукції, есе, дебатів, типових хиб та визначень).\n"
            )

        if "Ентоні Вестон (Anthony Weston)" not in idx_content:
            idx_content = idx_content.replace(
                "- [[Дуглас Волтон (Douglas Walton)]]\n",
                "- [[Дуглас Волтон (Douglas Walton)]]\n- [[Ентоні Вестон (Anthony Weston)]]\n"
            )

        # Build index addition
        by_folder = {}
        for entry in new_concept_entries:
            by_folder.setdefault(entry["folder"], []).append(entry)

        folder_titles = {
            "making_json_segments": "Making Your Case (Правила судової аргументації Скаліа та Гарнера)",
            "attaking_json-segments": "Attacking Faulty Reasoning (Логічні помилки та кодекс Деймера)",
            "logica_json_segments": "Підручник логіки (В. Щербина)",
            "scherbina_json_segments": "Юридична аргументація (О. Щербина)",
            "theory_json_segments": "Теорія права (Н. Макормік)",
            "douglas_json_segments": "Неформальна логіка: прагматичний підхід (Дуглас Волтон)",
            "rulebook_json_segments": "Посібник з аргументації (Ентоні Вестон)"
        }

        # Handle rulebook entries
        rulebook_entries = [e for e in new_concept_entries if e["folder"] == "rulebook_json_segments"]
        if rulebook_entries:
            addition = "\n\n---\n## Скомпільовані матеріали: Ентоні Вестон (A Rulebook for Arguments)\n\n"
            addition += "> Автор: [[Ентоні Вестон (Anthony Weston)]] · Праця: *A Rulebook for Arguments (5th Edition)*\n\n"
            by_sec = {}
            for e in rulebook_entries:
                by_sec.setdefault(e["section"] or "Інше", []).append(e)
            for sec, entries in by_sec.items():
                addition += f"### {sec}\n\n"
                for e in entries:
                    addition += f"- [{e['title']}](wiki/concepts/{e['title']}.md)\n"
                addition += "\n"
            idx_content += addition

        douglas_entries = [e for e in new_concept_entries if e["folder"] == "douglas_json_segments"]
        if douglas_entries:
            addition = "\n\n---\n## Скомпільовані матеріали: Дуглас Волтон (Informal Logic)\n\n"
            addition += "> Автор: [[Дуглас Волтон (Douglas Walton)]] · Праця: *Informal Logic: A Pragmatic Approach (2nd Edition)*\n\n"
            by_sec = {}
            for e in douglas_entries:
                by_sec.setdefault(e["section"] or "Інше", []).append(e)
            for sec, entries in by_sec.items():
                addition += f"### {sec}\n\n"
                for e in entries:
                    addition += f"- [{e['title']}](wiki/concepts/{e['title']}.md)\n"
                addition += "\n"
            idx_content += addition

        other_entries = [e for e in new_concept_entries if e["folder"] not in ["douglas_json_segments", "rulebook_json_segments"]]
        if other_entries:
            for fld, entries in by_folder.items():
                if fld in ["douglas_json_segments", "rulebook_json_segments"]:
                    continue
                sec_title = folder_titles.get(fld, fld)
                addition = f"\n### {sec_title}\n\n"
                for e in sorted(entries, key=lambda x: x['title']):
                    addition += f"- [{e['title']}](wiki/concepts/{e['title']}.md)\n"
                idx_content += addition

        with open(index_path, 'w', encoding='utf-8') as idx_w:
            idx_w.write(idx_content)

        # Append to log.md
        if rulebook_entries:
            with open(log_path, 'a', encoding='utf-8') as lg:
                lg.write(f"\n\n## [2026-09-18] ingest | Компіляція першоджерела Ентоні Вестона (A Rulebook for Arguments) за методом Karpathy LLM Wiki\n\n")
                lg.write(f"- **Дія**: Скомпільовано {len(rulebook_entries)} розділів та сегментів із каталогу `Clippings/rulebook_json_segments` у повноцінні статті `wiki/concepts/`.\n")
                lg.write(f"- **Джерело**: Ентоні Вестон, *«A Rulebook for Arguments»* (5th Edition, Hackett Publishing Company).\n")
                lg.write(f"- **Сутності**: Створено профіль автора `[[Ентоні Вестон (Anthony Weston)]]` у `wiki/entities/`.\n")
                lg.write(f"- **Результат**: Сформовано YAML-фронтматтери (теги, дати, джерела, групи), налаштовано системні зв'язки з батьківськими концептами та оновлено центральний `index.md`.\n")

if __name__ == "__main__":
    main()
