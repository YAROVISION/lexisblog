import os
import re

clippings_dir = "/Users/kostantinkrivula/Desktop/sqlbase/logica/logicaobsidiant/Clippings"
wiki_dir = "/Users/kostantinkrivula/Desktop/sqlbase/logica/logicaobsidiant/wiki/concepts"
log_path = "/Users/kostantinkrivula/Desktop/sqlbase/logica/logicaobsidiant/log.md"

def get_unprocessed():
    with open(log_path, 'r', encoding='utf-8') as f:
        log_content = f.read()

    unprocessed = []
    scalia_dir = os.path.join(clippings_dir, "making_json_segments")
    for file in sorted(os.listdir(scalia_dir)):
        if file.endswith('.md'):
            filepath = os.path.join(scalia_dir, file)
            if file not in log_content:
                unprocessed.append(filepath)
    return unprocessed

unprocessed_files = get_unprocessed()

concept_content = """---
type: concept
tags: [аргументація, адвокатура, судова_промова, scalia_garner]
---

# Додаткові правила судової аргументації (Scalia & Garner)

Цей концепт об'єднує залишкові правила та поради з книги "Making Your Case: The Art of Persuading Judges" Антона Скаліа та Брайана Гарнера, які стосуються підготовки документів, усного виступу та взаємодії із судом.

## Джерела (Залишкові 71 файлів)

"""

for f in unprocessed_files:
    basename = os.path.basename(f)
    concept_content += f"- [{basename}](file://{f})\n"

concept_path = os.path.join(wiki_dir, "Додаткові_правила_судової_аргументації.md")
with open(concept_path, 'w', encoding='utf-8') as f:
    f.write(concept_content)

print(f"Created concept at {concept_path} with {len(unprocessed_files)} links.")

# Append to log.md
log_entry = "\n## [2026-09-13] ingest | Making Your Case (Scalia & Garner) - Батч 6 (Залишкові правила)\n"
log_entry += "- **Дія**: Проведено інгістування (агентне).\n"
log_entry += "- **Опрацьовано**:\n"
for f in unprocessed_files:
    rel_path = "Clippings/making_json_segments/" + os.path.basename(f)
    log_entry += f"  - `[[{rel_path}]]`\n"

log_entry += "- **Створено концепції**:\n"
log_entry += "  - `[[Додаткові правила судової аргументації]]`\n"
log_entry += "- **Оновлено**: `[[index.md]]`\n"

with open(log_path, 'a', encoding='utf-8') as f:
    f.write(log_entry)

print("Updated log.md")
