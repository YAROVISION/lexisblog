#!/usr/bin/env python3
"""
link_neurobrain_segments.py
Connects all segments, sources, entities, concepts, and the master '00_Нейромозок.md' hub.
"""

import os
import re
import glob

VAULT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'digestobsidiant')
SEGMENTS_DIR = os.path.join(VAULT_DIR, 'segments')
SOURCES_DIR = os.path.join(VAULT_DIR, 'sources')
CONCEPTS_DIR = os.path.join(VAULT_DIR, 'concepts')
ENTITIES_DIR = os.path.join(VAULT_DIR, 'entities')

# Concept keywords mapping
CONCEPT_KEYWORDS = {
    'zemelni_spory': ['земельн', 'оренд.*земл', 'пай', 'сервітут.*зем'],
    'zahyst_vlasnosti': ['прав.*власност', 'віндикац', 'негаторн', 'витребуван.*майн', 'скасуван.*держреєстрац.*прав'],
    'trudovi_spory_ta_derzhsluzhba': ['трудов', 'звільнен', 'поновлен.*на.*робот', 'держслужб', 'заробітн.*плат', 'середній.*заробіт'],
    'dogovirni_pravovidnosyny': ['договір', 'зобов\'язан', 'недійсн.*правочин', 'форс-мажор', 'штраф', 'пеня', 'невиконан.*договор'],
    'podatkovi_ta_mytni_spory': ['податк', 'пдв', 'податков.*накладн', 'митн', 'митниц', 'митн.*вартіст'],
    'korporatyvni_spory': ['корпоративн', 'загальн.*збор', 'учасник.*товариств', 'частк.*у.*статутн', 'акціонер', 'наглядов.*рад'],
    'publichni_zakupivli': ['публічн.*закупівл', 'тендер', 'прозорро', 'договір.*про.*закупівл'],
    'suddivska_vynahoroda': ['суддівськ.*винагород', 'довічне.*грошов.*утриман', 'судд.*у.*відставц'],
    'sotsialni_prava': ['соціальн', 'пенсійн', 'пенсі', 'пільг', 'чорнобил', 'перерахунок.*пенс'],
    'vykonavche_provadzhennya': ['виконавч.*проваджен', 'державн.*виконав', 'приватн.*виконав', 'арешт.*майн', 'стягнен.*борг'],
    'protsesualni_pytannya': ['процесуальн', 'підсудност', 'строк.*звернен', 'позовн.*давніст', 'судов.*збір', 'забезпечен.*позов'],
    'yurysdyktsiyni_pytannya': ['юрисдикці', 'розмежуван.*юрисдикц', 'предметн.*юрисдикц'],
    'kryminalne_pravo_ta_protses': ['кримінальн', 'кпк', 'підозр', 'обвинувачен', 'запобіжн.*захід', 'кваліфікац.*злочин'],
    'viyskovyy_stan_ta_zahyst_batkivshchyny': ['воєнн.*стан', 'військов', 'мобілізац', 'військовослужбов', 'впо', 'збитки.*війн'],
    'espl_ta_mizhnarodne_pravo': ['єспл', 'конвенці', 'статт.*6.*конвенц', 'перш.*протокол', 'страсбург'],
    'bankrutstvo_ta_vidnovlennya_platospromozhnosti': ['банкрутств', 'неплатоспроможн', 'кодекс.*з.*процедур.*банкрутств', 'ліквідаційн', 'мораторій'],
    'intelektualna_vlasnist': ['інтелектуальн.*власност', 'авторськ.*прав', 'торговельн.*марк', 'патент', 'знак.*для.*товар'],
    'vidshkoduvannya_shkody': ['відшкодуван.*шкод', 'морально.*шкод', 'майново.*шкод', 'делікт', 'збитк']
}

# Entity keywords mapping
ENTITY_KEYWORDS = {
    'VP_VS': ['велик.*палат', 'вп.*вс', 'вп вс'],
    'KAS_VS': ['касаційн.*адміністративн', 'кас.*вс', 'кас вс'],
    'KGS_VS': ['касаційн.*господарськ', 'кгс.*вс', 'кгс вс'],
    'KCS_VS': ['касаційн.*цивільн', 'кцс.*вс', 'кцс вс'],
    'KKS_VS': ['касаційн.*кримінальн', 'ккс.*вс', 'ккс вс'],
    'ESPL': ['єспл', 'європейськ.*суд.*з.*прав.*людин'],
    'Prokuratura': ['прокуратур', 'прокурор'],
    'VRP_VKKS': ['вища.*рада.*правосуддя', 'врп', 'вккс', 'кваліфікаційн.*комісі.*суддів']
}

def extract_title_and_clean(content, filename):
    # Remove existing frontmatter if any
    clean = re.sub(r'^---[\s\S]*?---\n', '', content).strip()
    
    # Try finding first heading
    h_match = re.search(r'^#{1,4}\s+(.+)$', clean, re.M)
    # Try finding numbered section like 1.1. Title
    num_match = re.search(r'(?:^|\n)(\d+\.\d+\.?\s+[^\n]+)', clean)
    
    if num_match and len(num_match.group(1).strip()) > 5:
        title = num_match.group(1).strip()
    elif h_match and len(h_match.group(1).strip()) > 5:
        title = h_match.group(1).strip()
    else:
        # Fallback to first non-empty line
        lines = [l.strip() for l in clean.splitlines() if l.strip()]
        if lines:
            title = lines[0][:80]
        else:
            title = filename.replace('_', ' ').replace('.md', '')

    # Clean title
    title = re.sub(r'[#*`]', '', title).strip()
    if len(title) > 90:
        title = title[:87] + '...'
    if not title:
        title = filename.replace('_', ' ').replace('.md', '')
    return title, clean

def process_all():
    print("1. Creating / Updating 00_Нейромозок.md...")
    neuro_path = os.path.join(VAULT_DIR, '00_Нейромозок.md')
    neuro_content = """---
title: 🧠 Нейромозок Судової Практики (Master Nexus)
category: root
type: brain_core
last_updated: 2026-09-24
total_sources: 232
total_segments: 8873
---

# 🧠 Нейромозок Судової Практики — Центральне Ядро (Master Nexus)

Ласкаво просимо до цифрового ядра знань судової практики Верховного Суду та ЄСПЛ.
Нейромозок об'єднує **232 офіційні дайджести**, **8 873 аналітичні правові позиції (сегменти)**, **18 тематичних правових концепцій** та **8 ключових інституцій правосуддя**.

---

## 🏛️ Ключові Інституції та Судові Юрисдикції (Entities)
- [[VP_VS|Велика Палата Верховного Суду (ВП ВС)]] — забезпечення однакового застосування норм права, виключні правові проблеми.
- [[KAS_VS|Касаційний адміністративний суд (КАС ВС)]] — публічно-правові спори, податки, публічна служба, митниця.
- [[KGS_VS|Касаційний господарський суд (КГС ВС)]] — господарська діяльність, банкрутство, корпоративні спори.
- [[KCS_VS|Касаційний цивільний суд (КЦС ВС)]] — цивільні зобов'язання, захист власності, сімейні та земельні спори.
- [[KKS_VS|Касаційний кримінальний суд (ККС ВС)]] — кримінальне судочинство, кваліфікація правопорушень.
- [[ESPL|Європейський суд з прав людини (ЄСПЛ)]] — практика захисту прав і свобод за конвенційними нормами.
- [[Prokuratura|Органи прокуратури України]] — представництво інтересів держави в судах.
- [[VRP_VKKS|Вища рада правосуддя та ВККС]] — дисциплінарна практика та суддівське самоврядування.

---

## 📚 Тематичні Правові Хаби (Concepts)
- [[zemelni_spory|Земельні спори]]
- [[zahyst_vlasnosti|Захист права власності]]
- [[trudovi_spory_ta_derzhsluzhba|Трудові спори та державна служба]]
- [[dogovirni_pravovidnosyny|Договірні правовідносини та форс-мажор]]
- [[podatkovi_ta_mytni_spory|Податкові та митні спори]]
- [[korporatyvni_spory|Корпоративні спори та відповідальність керівників]]
- [[publichni_zakupivli|Публічні закупівлі]]
- [[suddivska_vynahoroda|Суддівська винагорода та статус суддів]]
- [[sotsialni_prava|Соціальні права та соціальний захист]]
- [[vykonavche_provadzhennya|Виконавче провадження та звернення стягнення]]
- [[protsesualni_pytannya|Процесуальні питання (ЦПК, ГПК, КАС, КПК)]]
- [[yurysdyktsiyni_pytannya|Розмежування судових юрисдикцій]]
- [[kryminalne_pravo_ta_protses|Кримінальне право та процес]]
- [[viyskovyy_stan_ta_zahyst_batkivshchyny|Правовий режим воєнного стану]]
- [[espl_ta_mizhnarodne_pravo|Практика ЄСПЛ у національному праві]]
- [[bankrutstvo_ta_vidnovlennya_platospromozhnosti|Банкрутство та неплатоспроможність]]
- [[intelektualna_vlasnist|Інтелектуальна власність]]
- [[vidshkoduvannya_shkody|Відшкодування збитків та делікти]]

---

## 📂 Зведені Каталоги та Сегменти
- [[index|Головний змістовний каталог (Index)]]
- [[sources/index|Повний реєстр 232 джерел дайджестів]]
- [[overview|Синтетичний огляд правових доктрин]]
"""
    with open(neuro_path, 'w', encoding='utf-8') as f:
        f.write(neuro_content)

    print("2. Processing all segments and adding backlinks...")
    digest_folders = sorted(os.listdir(SEGMENTS_DIR))
    
    seg_titles_map = {} # (digest, seg_stem) -> title

    for digest in digest_folders:
        digest_path = os.path.join(SEGMENTS_DIR, digest)
        if not os.path.isdir(digest_path):
            continue
        
        # Detect court entities matching digest name
        digest_entities = []
        for ent, kws in ENTITY_KEYWORDS.items():
            for kw in kws:
                if re.search(kw, digest, re.I):
                    if ent not in digest_entities:
                        digest_entities.append(ent)
                    break
        
        # Detect concepts matching digest name
        digest_concepts = []
        for con, kws in CONCEPT_KEYWORDS.items():
            for kw in kws:
                if re.search(kw, digest, re.I):
                    if con not in digest_concepts:
                        digest_concepts.append(con)
                    break

        for seg_file in sorted(os.listdir(digest_path)):
            if not seg_file.endswith('.md'):
                continue
            seg_stem = seg_file[:-3]
            file_full = os.path.join(digest_path, seg_file)
            
            with open(file_full, 'r', encoding='utf-8') as f:
                content = f.read()
            
            title, clean_content = extract_title_and_clean(content, seg_file)
            seg_titles_map[(digest, seg_stem)] = title
            
            # Content-specific entity detection
            matched_entities = list(digest_entities)
            for ent, kws in ENTITY_KEYWORDS.items():
                if ent not in matched_entities:
                    for kw in kws:
                        if re.search(kw, clean_content, re.I):
                            matched_entities.append(ent)
                            break
            
            # Content-specific concept detection
            matched_concepts = list(digest_concepts)
            for con, kws in CONCEPT_KEYWORDS.items():
                if con not in matched_concepts:
                    for kw in kws:
                        if re.search(kw, clean_content, re.I):
                            matched_concepts.append(con)
                            break

            # Build navigation and backlink footer
            footer_links = [
                f"[[00_Нейромозок|🧠 Нейромозок]]",
                f"[[sources/{digest}|📂 Дайджест: {digest}]]"
            ]
            for ent in matched_entities[:2]:
                footer_links.append(f"[[{ent}]]")
            for con in matched_concepts[:3]:
                footer_links.append(f"[[{con}]]")

            footer = "\n\n---\n\n### 🔗 Зв'язки Нейромозку\n" + " • ".join(footer_links) + "\n"
            
            # Check if clean_content already has footer
            if "### 🔗 Зв'язки Нейромозку" in clean_content:
                clean_content = clean_content.split("### 🔗 Зв'язки Нейромозку")[0].strip()

            new_file_content = f"""---
title: "{title.replace('"', "'")}"
category: segment
digest: {digest}
segment: {seg_stem}
---

{clean_content}{footer}"""

            with open(file_full, 'w', encoding='utf-8') as f:
                f.write(new_file_content)

    print("3. Updating sources/*.md to link all segments as wikilinks...")
    for digest in digest_folders:
        source_file = os.path.join(SOURCES_DIR, f"{digest}.md")
        if not os.path.exists(source_file):
            continue
        
        digest_path = os.path.join(SEGMENTS_DIR, digest)
        if not os.path.isdir(digest_path):
            continue
        
        seg_files = sorted([f for f in os.listdir(digest_path) if f.endswith('.md')])
        
        with open(source_file, 'r', encoding='utf-8') as f:
            src_txt = f.read()
            
        # Detect entities & concepts for source
        matched_entities = []
        for ent, kws in ENTITY_KEYWORDS.items():
            for kw in kws:
                if re.search(kw, digest, re.I):
                    if ent not in matched_entities:
                        matched_entities.append(ent)
                    break
        
        matched_concepts = []
        for con, kws in CONCEPT_KEYWORDS.items():
            for kw in kws:
                if re.search(kw, digest, re.I):
                    if con not in matched_concepts:
                        matched_concepts.append(con)
                    break

        # Build clean segment list with wikilinks
        seg_links_txt = ""
        for sf in seg_files:
            stem = sf[:-3]
            stitle = seg_titles_map.get((digest, stem), stem)
            seg_links_txt += f"- [[segments/{digest}/{stem}|{stitle}]]\n"

        ent_links = " • ".join([f"[[{e}]]" for e in matched_entities]) if matched_entities else "[[VP_VS]]"
        con_links = " • ".join([f"[[{c}]]" for c in matched_concepts]) if matched_concepts else "[[protsesualni_pytannya]]"

        new_source_content = f"""---
title: Дайджест {digest}
category: sources
digest_slug: {digest}
segments_count: {len(seg_files)}
last_updated: 2026-09-24
---

# 📂 Дайджест: {digest}

- **Нейромозок:** [[00_Нейромозок|🧠 Головне ядро]] • [[sources/index|Каталог джерел]]
- **Суд / Інституція:** {ent_links}
- **Тематичні категорії:** {con_links}
- **Кількість сегментів:** {len(seg_files)}

---

## 📑 Перелік правових позицій та сегментів ({len(seg_files)})
{seg_links_txt}
"""
        with open(source_file, 'w', encoding='utf-8') as f:
            f.write(new_source_content)

    print("4. Updating index.md...")
    index_path = os.path.join(VAULT_DIR, 'index.md')
    with open(index_path, 'r', encoding='utf-8') as f:
        idx_txt = f.read()
    if '[[00_Нейромозок' not in idx_txt:
        idx_txt = idx_txt.replace('# Каталог бази знань LLM Wiki\n', '# Каталог бази знань LLM Wiki\n\n[[00_Нейромозок|🧠 Відкрити Центральне Ядро Нейромозку]]\n\n')
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(idx_txt)

    print("Done linking all files!")

if __name__ == '__main__':
    process_all()
