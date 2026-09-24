# LLM Wiki Schema & Operational Guidelines

**Version:** 1.0.0  
**Pattern:** Karpathy LLM Wiki Architecture ([reference](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f))  
**Knowledge Domain:** Судова практика Верховного Суду України (ВП ВС, КАС ВС, КГС ВС, КЦС ВС, ККС ВС) та ЄСПЛ  
**Root Directory:** `wiki/`  
**Raw Source Directory:** `agents/segments/`

---

## 1. Архітектура Wiki

```
wiki/
├── AGENTS.md              # Цей файл конфігурації та правил для LLM-агента
├── SCHEMA.md              # Схема та правила структури (аліас)
├── index.md               # Зведений предметний та структурний каталог (Catalog)
├── log.md                 # Хронологічний журнал дій (append-only)
├── overview.md            # Загальний синтетичний огляд правових позицій
├── entities/              # Сторінки ключових суб'єктів, судів та органів
│   ├── VP_VS.md
│   ├── KAS_VS.md
│   ├── KGS_VS.md
│   ├── KCS_VS.md
│   ├── KKS_VS.md
│   ├── ESPL.md
│   └── Prokuratura.md
├── concepts/              # Сторінки правових доктрин, інститутів та категорій спорів
│   ├── zemelni_spory.md
│   ├── trudovi_spory.md
│   ├── zahyst_vlasnosti.md
│   └── ...
├── sources/               # MOC (Map of Content) для кожного з 232 дайджестів
└── tools/                 # Допоміжні утиліти для швидкого пошуку та перевірки (linting)
    ├── wiki_search.py
    └── wiki_lint.py
```

---

## 2. Операційні правила для LLM

### 2.1. Ingest (Додавання нового джерела)
Коли надходить новий дайджест або файл сегментів:
1. LLM читає сегменти з `agents/segments/<назва_папки>/`.
2. Створює сторінку опису джерела в `wiki/sources/<назва_папки>.md`.
3. Оновлює відповідні сторінки в `wiki/concepts/` та `wiki/entities/`, додаючи посилання `` та синтезуючи правові висновки.
4. Оновлює `wiki/index.md`.
5. Додає запис до `wiki/log.md` у форматі:
   ```markdown
   ## [2026-09-24] ingest | <Назва дайджесту> (<Кількість сегментів> сегментів)
   - Оновлено концепції: 
   - Оновлено суб'єкти: 
   ```

### 2.2. Query (Відповіді на запити користувача)
1. Агент спочатку перевіряє `wiki/index.md` або шукає через `wiki/tools/wiki_search.py`.
2. Звертається до відповідних сторінок `wiki/concepts/` та `wiki/entities/`.
3. Формує точну, структуровану відповідь із посиланнями на конкретні постанови, номери справ та дати.
4. Якщо запит привів до виявлення нового важливого синтезу / порівняння, результат зберігається як нова сторінка в `wiki/concepts/`.

### 2.3. Lint (Перевірка цілісності)
Періодично запускається `wiki/tools/wiki_lint.py` для:
- Виявлення неіснуючих посилань (broken wikilinks).
- Пошуку ізольованих сторінок (orphans).
- Перевірки суперечностей та відступів від попередніх правових позицій.

---

## 3. Стандарти розмітки та Frontmatter

Кожна сторінка у `wiki/concepts/` та `wiki/entities/` обов'язково містить YAML-метадані:
```yaml
---
title: Назва концепції / суб'єкта
category: concepts | entities | sources
last_updated: 2026-09-24
sources_count: 15
tags:
  - судова_практика
  - категорія_спору
---
```
