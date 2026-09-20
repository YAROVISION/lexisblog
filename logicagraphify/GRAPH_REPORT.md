# GRAPH_REPORT: Топологічний аналіз бази знань Graphify

Цей звіт сформовано автоматизованим аналітичним модулем **Graphify** для оцінки структурної цілісності, кластеризації та семантичної щільності знань із 482 першоджерел логіки, судової аргументації та теорії права.

---

## 1. Загальні метрики графа

| Метрика | Значення | Опис |
|---|---|---|
| **Всього вузлів (Nodes)** | `490` | Поняття, правила, логічні помилки, автори |
| **Всього ребер (Edges)** | `833` | Структуровані типізовані зв'язки |
| **Середня зв'язність (Avg Degree)** | `3.40` | Середня кількість зв'язків на один вузол |
| **EXTRACTED зв'язки** | `657` | Явні витяги з тексту та прямі авторські цитування |
| **INFERRED зв'язки** | `170` | Міждисциплінарні семантичні висновки (між авторами) |
| **AMBIGUOUS зв'язки** | `6` | Дискусійні теоретичні точки дотику |

---

## 2. Центральні вузли-хаби (God Nodes)

Вузли з найвищим показником **Degree Centrality** є фундаментальними опорними концептами всієї системи. Запити AI-агентів повинні стартувати з аналізу цих вузлів для збереження контексту:

| Ранг | Вузол / Концепт | Кластер | Тип | Зв'язність (Degree) |
|---|---|---|---|---|
| 1 | [[Антонін Скаліа (Antonin Scalia)]] | Legal Philosophers & Authors | `entity` | **124** |
| 2 | [[Браян Гарнер (Bryan A. Garner)]] | Legal Philosophers & Authors | `entity` | **124** |
| 3 | [[Т. Едвард Деймер (T. Edward Damer)]] | Logic Theorists & Logicians | `entity` | **109** |
| 4 | [[Дуглас Волтон (Douglas Walton)]] | Logic Theorists & Logicians | `entity` | **97** |
| 5 | [[Ентоні Вестон (Anthony Weston)]] | Logic Theorists & Logicians | `entity` | **74** |
| 6 | [[Арістотель (Aristotle)]] | Foundational Classical Logic | `entity` | **39** |
| 7 | [[Олена Щербина]] | Legal Philosophers & Authors | `entity` | **26** |
| 8 | [[Incompatible Premises (Несумісні засновки)]] | Fallacies & Faulty Reasoning (Damer) | `fallacy` | **16** |
| 9 | [[Faulty Analogy (Хибна аналогія)]] | Fallacies & Faulty Reasoning (Damer) | `fallacy` | **16** |
| 10 | [[Contradiction Between Premise and Conclusion (Суперечність між засновком і висновком)]] | Fallacies & Faulty Reasoning (Damer) | `fallacy` | **16** |
| 11 | [[Appeal to Irrelevant Authority (Апеляція до некомпетентного авторитету)]] | Fallacies & Faulty Reasoning (Damer) | `fallacy` | **15** |
| 12 | [[Post Hoc Fallacy (Помилка «Після цього — отже, з причини цього»)]] | Fallacies & Faulty Reasoning (Damer) | `fallacy` | **15** |
| 13 | [[Confusion of Cause and Effect (Змішування причини і наслідку)]] | Fallacies & Faulty Reasoning (Damer) | `fallacy` | **15** |
| 14 | [[Neglect of a Common Cause (Ігнорування спільної причини)]] | Fallacies & Faulty Reasoning (Damer) | `fallacy` | **15** |
| 15 | [[Insufficient Sample (Недостатня вибірка / поспішне узагальнення)]] | Fallacies & Faulty Reasoning (Damer) | `fallacy` | **15** |

---

## 3. Кластери знань (Domain Clusters)

Граф структуровано на 17 функціональних кластерів знань:

### ❖ MacCormick Legal Reasoning & Justification (13 вузлів, сер. зв'язність: 2.5)
- **Ключові вузли:** [[1. Дедуктивне виправдання та юридичний силогізм (Deductive justification)]], [[2. Проблема універсалізації та раціональна неупередженість (The problem of universalisation)]], [[2. Виправдання другого порядку: проблеми тлумачення, релевантності та класифікації (Second order justification)]], [[Перехід до аргументативної теорії: «Rhetoric and the Rule of Law» (2005)]], [[Підсумок: Еволюція від рафінованого позитивізму до постпозитивізму (Recapitulation)]], [[Повний покажчик приміток та бібліографічних посилань 1–101 (Notes & References)]]...
- **Першоджерела:** `theory_json_segments`

### ❖ Scherbina Legal Hermeneutics & Abduction (26 вузлів, сер. зв'язність: 2.1)
- **Ключові вузли:** [[Висновки до четвертого розділу]], [[2. Аналітичний та герменевтичний аспекти логічного аналізу юридичної аргументації]], [[Титул, реквізити та зміст дисертації]], [[4. Абдукція в юридичній аргументації]], [[1. Основні сучасні підходи до аналізу юридичної аргументації]], [[2. Специфіка розуміння царини логічного знання при аналізі юридичної аргументації]]...
- **Першоджерела:** `scherbina_json_segments`

### ❖ Weston Argumentation Rules (54 вузлів, сер. зв'язність: 3.1)
- **Ключові вузли:** [[Правило 8: Використовуйте репрезентативні приклади (Use representative examples)]], [[Правило 29: Досліджуйте проблему з усіх боків (Explore the issue)]], [[Огляд: Розділ I. Короткі аргументи: деякі загальні правила (Overview: Chapter I: Short Arguments: Some General Rules)]], [[Правило 33: Досліджуйте альтернативи (Explore alternatives)]], [[Правило 42: Енергійно розставляйте смислові дороговкази (Signpost energetically)]], [[Правило 40: Налаштовуйте слухачів на сприйняття (Ask for a hearing)]]...
- **Першоджерела:** `rulebook_json_segments`

### ❖ Argument Construction & Essays (20 вузлів, сер. зв'язність: 1.1)
- **Ключові вузли:** [[Примітка до п'ятого видання (Note to the Fifth Edition)]], [[Огляд: Розділ IX. Усні аргументи (Overview: Chapter IX: Oral Arguments)]], [[Зміст книги (Table of Contents)]], [[Огляд: Розділ III. Аргументи за аналогією (Overview: Chapter III: Arguments by Analogy)]], [[Вступ: У чому сенс аргументації? (What’s the point of arguing?)]], [[Огляд: Розділ IV. Аргументи від авторитету (Overview: Chapter IV: Arguments from Authority)]]...
- **Першоджерела:** `rulebook_json_segments`

### ❖ Categorical Logic & Syllogistics (32 вузлів, сер. зв'язність: 1.5)
- **Ключові вузли:** [[5. Значення логіки для правознавства та юридичної практики]], [[4. Недедуктивні умовиводи]], [[2. Предмет науки логіки]], [[4. Відношення між поняттями. Діаграми Ейлера – Венна]], [[Контрольні питання до Розділу 2]], [[5. Логіка запитань і відповідей (інтерогативна логіка)]]...
- **Першоджерела:** `logica_json_segments`

### ❖ Formal Logic Laws & Rules (7 вузлів, сер. зв'язність: 1.3)
- **Ключові вузли:** [[3. Правила доведення та можливі логічні помилки в доведенні]], [[3. Закон непротиріччя]], [[4. Закон виключеного третього]], [[2. Логічна структура поняття. Закон зворотного відношення між змістом і обсягом поняття]], [[5. Закон достатньої підстави]], [[1. Загальна характеристика основних законів логіки]]...
- **Першоджерела:** `logica_json_segments`

### ❖ Scalia & Garner Legal Persuasion (115 вузлів, сер. зв'язність: 2.5)
- **Ключові вузли:** [[Знати, як використовувати та структурувати частини меморандуму]], [[Спробуйте знайти явне формулювання вашої основної передумови у керуючих або переконливих справах.]], [[Прагніть здобути репутацію досконалості]], [[Ніколи не питайте, скільки часу у вас залишилось.]], [[Опануйте відносну вагу прецедентів.]], [[Знай свій справи.]]...
- **Першоджерела:** `making_json_segments`

### ❖ Judicial Advocacy & Briefing (9 вузлів, сер. зв'язність: 2.0)
- **Ключові вузли:** [[Передмова (Голови Верховного Суду США Джона Г. Робертса)]], [[Огляд - Підготовка письмових матеріалів]], [[Рекомендовані джерела та література]], [[Джерела цитат у тексті]], [[Огляд - Юридичне мислення]], [[Огляд - Загальні принципи аргументації]]...
- **Першоджерела:** `making_json_segments`

### ❖ Dialogue Theory & Pragma-Dialectics (85 вузлів, сер. зв'язність: 1.0)
- **Ключові вузли:** [[7. Важливі типи помилок для перевірки (Important Types of Error to Check)]], [[Дуглас Уолтон — Неформальна логіка: прагматичний підхід]], [[5. Інвалідні (невалідні) аргументи (Invalid Arguments)]], [[3. «Ви перестали бити дружину?»]], [[5. Аргумент post hoc (The Post Hoc Argument)]], [[6. Критика аргументів за аналогією (Criticizing Arguments from Analogy)]]...
- **Першоджерела:** `douglas_json_segments`

### ❖ Pragmatic Fallacies (Walton) (8 вузлів, сер. зв'язність: 1.5)
- **Ключові вузли:** [[Вступ до глави 8: Індуктивні помилки, упередження та софізми (Inductive Errors, Bias, and Fallacies)]], [[6. Критичні запитання до ad hominem аргументу (Critical Questions for an Ad Hominem Argument)]], [[7. Помилки композиції та поділу (Composition and Division)]], [[4. Непомилкові ad hominem аргументи (Non-Fallacious Ad Hominem Arguments)]], [[1. Образливий ad hominem аргумент (The Abusive Ad Hominem Argument)]], [[2. Навантажені терміни та мова з передрішенням тези (Loaded Terms and Question-Begging Language)]]...
- **Першоджерела:** `douglas_json_segments`

### ❖ Walton Argumentation Schemes (4 вузлів, сер. зв'язність: 1.0)
- **Ключові вузли:** [[10. Правила запитань і відповідей у діалозі]], [[5. Відволікання («червоний оселедець») проти неправильного висновку (Red Herring vs. Wrong Conclusion)]], [[2. Схема аргументації для апеляції до експертної думки (Argumentation Scheme for Appeal to Expert Opinion)]], [[4. Негативні правила діалогу переконання]]...
- **Першоджерела:** `douglas_json_segments`

### ❖ Fallacies & Faulty Reasoning (Damer) (88 вузлів, сер. зв'язність: 3.4)
- **Ключові вузли:** [[Каузальні помилки: огляд (Causal Fallacies: Overview)]], [[Помилки нерелевантної апеляції: огляд (Fallacies of Irrelevant Appeal: Overview)]], [[Fallacy of Composition (Помилка композиції / хибне об'єднання)]], [[Вправи: Помилки необґрунтованого припущення (Assignments: Unwarranted Assumption)]], [[Appeal to Self-Interest (Апеляція до особистого інтересу / егоїзму)]], [[Fallacy of Division (Помилка дивізії / хибний поділ)]]...
- **Першоджерела:** `attaking_json-segments`

### ❖ Damer Critical Thinking (18 вузлів, сер. зв'язність: 1.2)
- **Ключові вузли:** [[Титул, вихідні дані та зміст (Title, Copyright & Contents)]], [[Принципи утримання від судження та розв'язання спору (Suspension of Judgment & Resolution)]], [[Тягар доведення та стандартна форма аргументу (Burden of Proof & Standard Form)]], [[Ціннісні аргументи: моральні, правові та естетичні (Moral, Legal, and Aesthetic Arguments)]], [[Покажчик]], [[Вправи до Глави 10 (Assignments: Writing the Argumentative Essay)]]...
- **Першоджерела:** `attaking_json-segments`

### ❖ Argumentation Principles & Ethics (3 вузлів, сер. зв'язність: 1.0)
- **Ключові вузли:** [[Процедурний та етичний стандарт дискусії (An Effective Procedural & Ethical Standard)]], [[Вправи до Глави 1 (Assignments: A Code of Intellectual Conduct)]], [[Принципи 1-3: Помильність, пошук істини та ясність (Principles 1-3: Fallibility, Truth-Seeking, Clarity)]]...
- **Першоджерела:** `attaking_json-segments`

### ❖ Legal Philosophers & Authors (4 вузлів, сер. зв'язність: 71.8)
- **Ключові вузли:** [[Ніл Маккормік (Neil MacCormick)]], [[Антонін Скаліа (Antonin Scalia)]], [[Браян Гарнер (Bryan A. Garner)]], [[Олена Щербина]]...
- **Першоджерела:** `entities`

### ❖ Logic Theorists & Logicians (3 вузлів, сер. зв'язність: 93.3)
- **Ключові вузли:** [[Дуглас Волтон (Douglas Walton)]], [[Т. Едвард Деймер (T. Edward Damer)]], [[Ентоні Вестон (Anthony Weston)]]...
- **Першоджерела:** `entities`

### ❖ Foundational Classical Logic (1 вузлів, сер. зв'язність: 39.0)
- **Ключові вузли:** [[Арістотель (Aristotle)]]...
- **Першоджерела:** `entities`


---

## 4. Інструкція для AI-агентів (Agent Context Optimization)

1. **Мінімізація контекстного вікна:** Замість послідовного завантаження сотень сирих файлів кліпінгів, агент зчитує `GRAPH_REPORT.md` та `graph.json`.
2. **Маршрутизація запитів (Graph Traversal):**
   - Для питань з **судової аргументації**: починати з кластерів *Scalia & Garner Legal Persuasion* та *MacCormick Legal Reasoning*.
   - Для виявлення **помилок у процесуальних документах**: проходити через ребра `VIOLATES_RULE` між кластерами *Fallacies & Faulty Reasoning* та *Argumentation Principles*.
   - Для перевірки **доказової бази**: використовувати вузли *Абдукція в праві* та *Юридичний силогізм*.
3. **Оцінка надійності:** Враховувати рівні впевненості `EXTRACTED` як аксіоматичні, а `INFERRED` — як аргументативні гіпотези.
