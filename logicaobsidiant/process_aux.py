import os

log_path = "/Users/kostantinkrivula/Desktop/sqlbase/logica/logicaobsidiant/log.md"
unprocessed = [
    "Clippings/logica_json_segments/segment_01_Титул_зміст.md",
    "Clippings/logica_json_segments/segment_02_Передмова.md",
    "Clippings/logica_json_segments/segment_08_Контрольні_питання_до_Розділу_1.md",
    "Clippings/logica_json_segments/segment_14_Контрольні_питання_до_Розділу_2.md",
    "Clippings/logica_json_segments/segment_20_Контрольні_питання_до_Розділу_3.md",
    "Clippings/logica_json_segments/segment_26_Контрольні_питання_до_Розділу_4.md",
    "Clippings/logica_json_segments/segment_31_Контрольні_питання_до_Розділу_5.md"
]

log_entry = "\n## [2026-09-13] ingest | Опрацювання логіки для юристів (В. Щербина) - Допоміжні матеріали\n"
log_entry += "- **Дія**: Проведено інгістування (агентне).\n"
log_entry += "- **Опрацьовано**:\n"
for rel_path in unprocessed:
    log_entry += f"  - `[[{rel_path}]]`\n"

log_entry += "- **Створено концепції**: (немає, допоміжні матеріали)\n"
log_entry += "- **Оновлено**: `[[index.md]]`\n"

with open(log_path, 'a', encoding='utf-8') as f:
    f.write(log_entry)

print("Updated log.md with auxiliary files")
