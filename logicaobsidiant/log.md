# Журнал операцій LLM Wiki (Audit Ledger)

Хронологічний реєстр усіх дій (ingest, query, lint), виконаних агентом у цій базі знань.

---

## [2026-09-13] init | Ініціалізація системи LLM Wiki (Karpathy System)

- **Дія**: Створено базову трирівневу структуру ваулту.
- **Джерела**: Підключено каталог `Clippings/` (5 підпапок сегментів).
- **Створено**:
  - `index.md` — головний навігаційний каталог.
  - `log.md` — журнал операцій.
  - `conventions.md` — правила та стандарти бази.
  - Скіл агента: `.agents/skills/llm-wiki/SKILL.md`.

## [2026-09-13] ingest | Опрацювання теорії аргументації (Макормік)

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/theory_json_segments/segment_004_2.1._Deductive_justification.md]]`
  - `[[Clippings/theory_json_segments/segment_005_2.2._Second_order_justification.md]]`
  - `[[Clippings/theory_json_segments/segment_006_2.3._Consequentialist_arguments.md]]`
- **Створено концепції**:
  - `[[Дедуктивне виправдання]]`
  - `[[Виправдання другого порядку]]`
  - `[[Консеквенціалістський аргумент]]`
  - `[[Когерентність правової системи]]`
- **Створено сутності**:
  - `[[Макормік (Neil MacCormick)]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Опрацювання теорії аргументації (Батч 2)

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/theory_json_segments/segment_007_3._Rhetoric_and_the_Rule_of_Law_2005.md]]`
  - `[[Clippings/theory_json_segments/segment_008_3.1._Rhetoric_and_the_rule_of_law.md]]`
  - `[[Clippings/theory_json_segments/segment_009_3.2._The_problem_of_universalisation.md]]`
  - `[[Clippings/theory_json_segments/segment_010_3.3._Approximation_to_Dworkin_s_thesis.md]]`
  - `[[Clippings/theory_json_segments/segment_011_3.4._Application_of_the_deductive_model.md]]`
- **Створено концепції**:
  - `[[Універсалізація]]`
  - `[[Верховенство права]]`
  - `[[Складні та ясні справи]]`
- **Оновлено концепції**:
  - `[[Дедуктивне виправдання]]`
- **Створено сутності**:
  - `[[Дворкін (Ronald Dworkin)]]`
- **Оновлено сутності**:
  - `[[Макормік (Neil MacCormick)]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Опрацювання теорії аргументації (Батч 3)

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/theory_json_segments/segment_001_Title_and_Abstract.md]]`
  - `[[Clippings/theory_json_segments/segment_002_1._Introduction.md]]`
  - `[[Clippings/theory_json_segments/segment_003_2._Legal_Reasoning_and_Legal_Theory_1978.md]]`
  - `[[Clippings/theory_json_segments/segment_012_4._Recapitulation.md]]`
  - `[[Clippings/theory_json_segments/segment_013_Notes_and_References.md]]`
- **Створено концепції**:
  - `[[Юридичний позитивізм]]`
  - `[[Постпозитивізм]]`
  - `[[Діахронічний підхід]]`
- **Створено сутності**:
  - `[[Гарт (H.L.A. Hart)]]`
- **Оновлено сутності**:
  - `[[Макормік (Neil MacCormick)]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Опрацювання логіки для юристів (В. Щербина) - Батч 1

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/logica_json_segments/segment_03_1.1._Поняття_про_мислення.md]]`
  - `[[Clippings/logica_json_segments/segment_04_1.2._Предмет_науки_логіки.md]]`
  - `[[Clippings/logica_json_segments/segment_05_1.3._Історичні_етапи_розвитку_науки_логіки.md]]`
  - `[[Clippings/logica_json_segments/segment_06_1.4._Мислення_і_мова._Семіотика.md]]`
  - `[[Clippings/logica_json_segments/segment_07_1.5._Значення_логіки_для_правознавства_та_юридично.md]]`
- **Створено концепції**:
  - `[[Логіка (як наука)]]`
  - `[[Історія логіки]]`
  - `[[Мислення]]`
  - `[[Семіотика]]`
- **Створено сутності**:
  - `[[Арістотель (Aristotle)]]`
  - `[[Френсіс Бекон (Francis Bacon)]]`
  - `[[Чарльз Пірс (Charles Peirce)]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Опрацювання логіки для юристів (В. Щербина) - Батч 2

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/logica_json_segments/segment_09_2.1._Поняття_як_форма_думки._Поняття_і_слово.md]]`
  - `[[Clippings/logica_json_segments/segment_10_2.2._Логічна_структура_поняття._Закон_зворотного_в.md]]`
  - `[[Clippings/logica_json_segments/segment_11_2.3._Види_понять.md]]`
  - `[[Clippings/logica_json_segments/segment_12_2.4._Відношення_між_поняттями._Діаграми_Ейлера_Вен.md]]`
  - `[[Clippings/logica_json_segments/segment_13_2.5._Логічні_операції_з_поняттями.md]]`
- **Створено концепції**:
  - `[[Поняття (логіка)]]`
  - `[[Відношення між поняттями]]`
  - `[[Логічні операції з поняттями]]`
  - `[[Поділ поняття (Класифікація)]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Опрацювання логіки для юристів (В. Щербина) - Батч 3

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/logica_json_segments/segment_15_3.1._Загальна_характеристика_судження.md]]`
  - `[[Clippings/logica_json_segments/segment_16_3.2._Прості_судження.md]]`
  - `[[Clippings/logica_json_segments/segment_17_3.3._Складні_судження.md]]`
  - `[[Clippings/logica_json_segments/segment_18_3.4._Модальні_судження.md]]`
  - `[[Clippings/logica_json_segments/segment_19_3.5._Логіка_запитань_і_відповідей_інтерогативна_ло.md]]`
- **Створено концепції**:
  - `[[Судження]]`
  - `[[Прості судження (категоричні)]]`
  - `[[Складні судження]]`
  - `[[Модальні судження]]`
  - `[[Логіка запитань і відповідей (Інтерогативна логіка)]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Опрацювання логіки для юристів (В. Щербина) - Батч 4

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/logica_json_segments/segment_21_4.1._Загальна_характеристика_основних_законів_логі.md]]`
  - `[[Clippings/logica_json_segments/segment_22_4.2._Закон_тотожності.md]]`
  - `[[Clippings/logica_json_segments/segment_23_4.3._Закон_непротиріччя.md]]`
  - `[[Clippings/logica_json_segments/segment_24_4.4._Закон_виключеного_третього.md]]`
  - `[[Clippings/logica_json_segments/segment_25_4.5._Закон_достатньої_підстави.md]]`
- **Створено концепції**:
  - `[[Закони логіки]]`
  - `[[Закон тотожності]]`
  - `[[Закон непротиріччя]]`
  - `[[Закон виключеного третього]]`
  - `[[Закон достатньої підстави]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Опрацювання логіки для юристів (В. Щербина) - Батч 5

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/logica_json_segments/segment_27_5.1._Загальна_характеристика_умовиводів._Види_умов.md]]`
  - `[[Clippings/logica_json_segments/segment_28_5.2._Безпосередні_умовиводи.md]]`
  - `[[Clippings/logica_json_segments/segment_29_5.3._Дедуктивні_умовиводи.md]]`
  - `[[Clippings/logica_json_segments/segment_30_5.4._Недедуктивні_умовиводи.md]]`
- **Створено концепції**:
  - `[[Умовивід]]`
  - `[[Дедуктивні умовиводи]]`
  - `[[Безпосередні умовиводи]]`
  - `[[Недедуктивні умовиводи]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Опрацювання логіки для юристів (В. Щербина) - Батч 6

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/logica_json_segments/segment_32_6.1._Загальна_характеристика_доведення.md]]`
  - `[[Clippings/logica_json_segments/segment_33_6.2._Види_доведення.md]]`
  - `[[Clippings/logica_json_segments/segment_34_6.3._Правила_доведення_та_можливі_логічні_помилки_.md]]`
  - `[[Clippings/logica_json_segments/segment_35_6.4._Спростування._Методи_спростування.md]]`
  - `[[Clippings/logica_json_segments/segment_36_6.5._Гіпотеза_як_форма_пізнання.md]]`
- **Створено концепції**:
  - `[[Доведення]]`
  - `[[Правила і помилки доведення]]`
  - `[[Спростування]]`
  - `[[Гіпотеза]]`
  - `[[Версія]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Опрацювання логіки для юристів (В. Щербина) - Фінальний батч

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/logica_json_segments/segment_37_Контрольні_питання_до_Розділу_6.md]]`
  - `[[Clippings/logica_json_segments/segment_38_Список_рекомендованих_джерел.md]]`
  - `[[Clippings/logica_json_segments/segment_39_Для_нотаток.md]]`
- **Створено концепції**:
  - `[[Література]]` (Список джерел)
- **Оновлено**: `[[index.md]]`
- **СТАТУС**: ПРОЦЕС ІНГІСТУВАННЯ ПІДРУЧНИКА ЗАВЕРШЕНО.

## [2026-09-13] ingest | Логічний аналіз юридичної аргументації (О. Щербина) - Батч 1

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/scherbina_json_segments/segment_01_Титул_та_зміст.md]]`
  - `[[Clippings/scherbina_json_segments/segment_02_Вступ.md]]`
  - `[[Clippings/scherbina_json_segments/segment_03_Розділ_1_1.1_Поняття_аргументації.md]]`
  - `[[Clippings/scherbina_json_segments/segment_04_Розділ_1_1.2_Історичні_взаємозв_язки.md]]`
  - `[[Clippings/scherbina_json_segments/segment_05_Розділ_1_Висновки.md]]`
- **Створено концепції**:
  - `[[Аргументація]]`
  - `[[Юридична аргументація]]`
  - `[[Логічний аналіз]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Логічний аналіз юридичної аргументації (О. Щербина) - Батч 2

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/scherbina_json_segments/segment_06_Розділ_2_2.1_Методологічна_функція_аргументації.md]]`
  - `[[Clippings/scherbina_json_segments/segment_07_Розділ_2_2.2_Специфіка_розуміння_царини_логічного.md]]`
  - `[[Clippings/scherbina_json_segments/segment_08_Розділ_2_2.3_Юридична_логіка_як_наукова_дисципліна.md]]`
  - `[[Clippings/scherbina_json_segments/segment_09_Розділ_2_Висновки.md]]`
- **Створено концепції**:
  - `[[Методологічна функція аргументації]]`
  - `[[Юридична логіка]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Логічний аналіз юридичної аргументації (О. Щербина) - Батч 3

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/scherbina_json_segments/segment_10_Розділ_3_3.1_Основні_сучасні_підходи.md]]`
  - `[[Clippings/scherbina_json_segments/segment_11_Розділ_3_3.2_Аналітичний_та_герменевтичний_аспекти.md]]`
  - `[[Clippings/scherbina_json_segments/segment_12_Розділ_3_3.3_Логічна_складова_правового_стилю.md]]`
  - `[[Clippings/scherbina_json_segments/segment_13_Розділ_3_Висновки.md]]`
  - `[[Clippings/scherbina_json_segments/segment_14_Розділ_4_4.1_Склад_та_способи_аргументації.md]]`
- **Створено концепції**:
  - `[[Підходи до аналізу юридичної аргументації]]`
  - `[[Аспекти логічного аналізу]]`
  - `[[Логічна складова правового стилю]]`
  - `[[Склад та способи аргументації]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Логічний аналіз юридичної аргументації (О. Щербина) - Батч 4

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/scherbina_json_segments/segment_15_Розділ_4_4.2_Дедукція_та_індукція_в_аргументації.md]]`
  - `[[Clippings/scherbina_json_segments/segment_16_Розділ_4_4.3_Специфіка_використання_аналогії.md]]`
  - `[[Clippings/scherbina_json_segments/segment_17_Розділ_4_4.4_Абдукція_в_юридичній_аргументації.md]]`
  - `[[Clippings/scherbina_json_segments/segment_18_Розділ_4_4.5_Феномен_мовчання_в_аргументації.md]]`
  - `[[Clippings/scherbina_json_segments/segment_19_Розділ_4_Висновки.md]]`
- **Створено концепції**:
  - `[[Дедукція та індукція в юридичній аргументації]]`
  - `[[Аналогія в юридичній аргументації]]`
  - `[[Абдукція в юридичній аргументації]]`
  - `[[Мовчання та обман в аргументації]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Логічний аналіз юридичної аргументації (О. Щербина) - Батч 5

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/scherbina_json_segments/segment_20_Розділ_5_5.1_Інтерпретація_та_тлумачення.md]]`
  - `[[Clippings/scherbina_json_segments/segment_21_Розділ_5_5.2_Двозначність_та_неясність.md]]`
  - `[[Clippings/scherbina_json_segments/segment_22_Розділ_5_5.3_Можливі_шляхи_подолання.md]]`
  - `[[Clippings/scherbina_json_segments/segment_23_Розділ_5_5.4_Проблема_визначення_кримінально_правової_норми.md]]`
  - `[[Clippings/scherbina_json_segments/segment_24_Розділ_5_Висновки.md]]`
  - `[[Clippings/scherbina_json_segments/segment_25_Загальні_висновки_дисертації.md]]`
  - `[[Clippings/scherbina_json_segments/segment_26_Список_літератури.md]]`
- **Створено концепції**:
  - `[[Герменевтичний аспект логічного аналізу]]`
  - `[[Семантична інтерпретація в праві]]`
- **Оновлено**: `[[index.md]]`, `[[Література.md]]`

## [2026-09-13] ingest | Атака на хибні міркування (Т. Е. Деймер) - Батч 1

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/attaking_json-segments/segment_001_Title_Copyright_and_Contents.md]]`
  - `[[Clippings/attaking_json-segments/segment_002_Preface_and_About_the_Author.md]]`
  - `[[Clippings/attaking_json-segments/segment_003_Introduction_Studying_Logic_and_Goals.md]]`
  - `[[Clippings/attaking_json-segments/segment_004_Ch1_Procedural_and_Ethical_Standard.md]]`
  - `[[Clippings/attaking_json-segments/segment_005_Ch1_Principles_1_to_3.md]]`
  - `[[Clippings/attaking_json-segments/segment_006_Ch1_Assignments.md]]`
- **Створено концепції**:
  - `[[Кодекс інтелектуальної поведінки]]`
  - `[[П'ять критеріїв хорошого аргументу]]`
- **Оновлено**: `[[index.md]]`, `[[Література.md]]`

## [2026-09-13] ingest | Атака на хибні міркування (Т. Е. Деймер) - Батч 2

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/attaking_json-segments/segment_007_Ch2_Argument_vs_Opinion.md]]`
  - `[[Clippings/attaking_json-segments/segment_008_Ch2_Burden_of_Proof_and_Standard_Form.md]]`
  - `[[Clippings/attaking_json-segments/segment_009_Ch2_Charity_Deductive_Inductive.md]]`
  - `[[Clippings/attaking_json-segments/segment_010_Ch2_Moral_Legal_Aesthetic_Arguments.md]]`
  - `[[Clippings/attaking_json-segments/segment_011_Ch2_Assignments.md]]`
- **Створено концепції**:
  - `[[Поняття аргументу]]`
  - `[[Дедуктивні та індуктивні аргументи]]`
  - `[[Ціннісні аргументи]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Атака на хибні міркування (Т. Е. Деймер) - Батч 3

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/attaking_json-segments/segment_012_Ch3_Five_Criteria_and_Structural_Principle.md]]`
  - `[[Clippings/attaking_json-segments/segment_013_Ch3_Relevance_Acceptability_Sufficiency_Rebuttal.md]]`
  - `[[Clippings/attaking_json-segments/segment_014_Ch3_Strengthening_and_Applying_Criteria.md]]`
  - `[[Clippings/attaking_json-segments/segment_015_Ch3_Suspension_of_Judgment_and_Resolution.md]]`
  - `[[Clippings/attaking_json-segments/segment_016_Ch3_Assignments.md]]`
- **Створено/Оновлено концепції**:
  - `[[П'ять критеріїв хорошого аргументу]]` (суттєво розширено)
  - `[[Принципи утримання від судження та розв'язання]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Атака на хибні міркування (Т. Е. Деймер) - Батч 4

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/attaking_json-segments/segment_017_Ch4_Theory_and_Organization_of_Fallacies.md]]`
  - `[[Clippings/attaking_json-segments/segment_018_Ch4_Attacking_the_Fallacy_and_Rules.md]]`
  - `[[Clippings/attaking_json-segments/segment_019_Ch4_Assignments.md]]`
- **Створено концепції**:
  - `[[Поняття логічної помилки]]`
  - `[[Методи критики логічних помилок]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Атака на хибні міркування (Т. Е. Деймер) - Батч 5

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/attaking_json-segments/segment_020_Ch5_Begging_the_Question_Overview.md]]`
  - `[[Clippings/attaking_json-segments/segment_021_Ch5_01_Arguing_in_a_Circle.md]]`
  - `[[Clippings/attaking_json-segments/segment_022_Ch5_02_Question_Begging_Language.md]]`
  - `[[Clippings/attaking_json-segments/segment_023_Ch5_03_Complex_Question.md]]`
  - `[[Clippings/attaking_json-segments/segment_024_Ch5_04_Question_Begging_Definition.md]]`
  - `[[Clippings/attaking_json-segments/segment_025_Ch5_Assignments_Begging_the_Question.md]]`
  - `[[Clippings/attaking_json-segments/segment_026_Ch5_Inconsistency_Overview.md]]`
  - `[[Clippings/attaking_json-segments/segment_027_Ch5_05_Incompatible_Premises.md]]`
  - `[[Clippings/attaking_json-segments/segment_028_Ch5_06_Contradiction_Premise_Conclusion.md]]`
  - `[[Clippings/attaking_json-segments/segment_029_Ch5_Assignments_Inconsistency.md]]`
  - `[[Clippings/attaking_json-segments/segment_030_Ch5_Deductive_Inference_Overview.md]]`
  - `[[Clippings/attaking_json-segments/segment_031_Ch5_07_Denying_the_Antecedent.md]]`
  - `[[Clippings/attaking_json-segments/segment_032_Ch5_08_Affirming_the_Consequent.md]]`
  - `[[Clippings/attaking_json-segments/segment_033_Ch5_09_False_Conversion.md]]`
  - `[[Clippings/attaking_json-segments/segment_034_Ch5_10_Undistributed_Middle_Term.md]]`
  - `[[Clippings/attaking_json-segments/segment_035_Ch5_11_Illicit_Distribution_End_Term.md]]`
  - `[[Clippings/attaking_json-segments/segment_036_Ch5_Assignments_Deductive_Inference.md]]`
- **Створено концепції**:
  - `[[Структурні помилки]]`
  - `[[Підміна питання (Begging the Question)]]`
  - `[[Помилки несумісності]]`
  - `[[Помилки дедуктивного виведення]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Атака на хибні міркування (Т. Е. Деймер) - Батч 6

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/attaking_json-segments/segment_037_Ch6_Irrelevant_Premise_Overview.md]]`
  - `[[Clippings/attaking_json-segments/segment_038_Ch6_12_Genetic_Fallacy.md]]`
  - `[[Clippings/attaking_json-segments/segment_039_Ch6_13_Rationalization.md]]`
  - `[[Clippings/attaking_json-segments/segment_040_Ch6_14_Drawing_the_Wrong_Conclusion.md]]`
  - `[[Clippings/attaking_json-segments/segment_041_Ch6_15_Using_the_Wrong_Reasons.md]]`
  - `[[Clippings/attaking_json-segments/segment_042_Ch6_Assignments_Irrelevant_Premise.md]]`
  - `[[Clippings/attaking_json-segments/segment_043_Ch6_Irrelevant_Appeal_Overview.md]]`
  - `[[Clippings/attaking_json-segments/segment_044_Ch6_16_Appeal_to_Irrelevant_Authority.md]]`
  - `[[Clippings/attaking_json-segments/segment_045_Ch6_17_Appeal_to_Common_Opinion.md]]`
  - `[[Clippings/attaking_json-segments/segment_046_Ch6_18_Appeal_to_Force_or_Threat.md]]`
  - `[[Clippings/attaking_json-segments/segment_047_Ch6_19_Appeal_to_Tradition.md]]`
  - `[[Clippings/attaking_json-segments/segment_048_Ch6_20_Appeal_to_Self_Interest.md]]`
  - `[[Clippings/attaking_json-segments/segment_049_Ch6_21_Manipulation_of_Emotions.md]]`
  - `[[Clippings/attaking_json-segments/segment_050_Ch6_Assignments_Irrelevant_Appeal.md]]`
- **Створено концепції**:
  - `[[Помилки релевантності]]`
  - `[[Нерелевантний засновок]]`
  - `[[Нерелевантна апеляція]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Атака на хибні міркування (Т. Е. Деймер) - Батч 7

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/attaking_json-segments/segment_051_Ch7_Linguistic_Confusion_Overview.md]]`
  - `[[Clippings/attaking_json-segments/segment_052_Ch7_22_Equivocation.md]]`
  - `[[Clippings/attaking_json-segments/segment_053_Ch7_23_Ambiguity.md]]`
  - `[[Clippings/attaking_json-segments/segment_054_Ch7_24_Misleading_Accent.md]]`
  - `[[Clippings/attaking_json-segments/segment_055_Ch7_25_Illicit_Contrast.md]]`
  - `[[Clippings/attaking_json-segments/segment_056_Ch7_26_Argument_by_Innuendo.md]]`
  - `[[Clippings/attaking_json-segments/segment_057_Ch7_27_Misuse_of_a_Vague_Expression.md]]`
  - `[[Clippings/attaking_json-segments/segment_058_Ch7_28_Distinction_Without_a_Difference.md]]`
  - `[[Clippings/attaking_json-segments/segment_059_Ch7_Assignments_Linguistic_Confusion.md]]`
  - `[[Clippings/attaking_json-segments/segment_060_Ch7_Unwarranted_Assumption_Overview.md]]`
  - `[[Clippings/attaking_json-segments/segment_061_Ch7_29_Fallacy_of_the_Continuum.md]]`
  - `[[Clippings/attaking_json-segments/segment_062_Ch7_30_Fallacy_of_Composition.md]]`
  - `[[Clippings/attaking_json-segments/segment_063_Ch7_31_Fallacy_of_Division.md]]`
  - `[[Clippings/attaking_json-segments/segment_064_Ch7_32_False_Alternatives.md]]`
  - `[[Clippings/attaking_json-segments/segment_065_Ch7_33_Is_Ought_Fallacy.md]]`
  - `[[Clippings/attaking_json-segments/segment_066_Ch7_34_Wishful_Thinking.md]]`
  - `[[Clippings/attaking_json-segments/segment_067_Ch7_35_Misuse_of_a_Principle.md]]`
  - `[[Clippings/attaking_json-segments/segment_068_Ch7_36_Fallacy_of_the_Mean.md]]`
  - `[[Clippings/attaking_json-segments/segment_069_Ch7_37_Faulty_Analogy.md]]`
  - `[[Clippings/attaking_json-segments/segment_070_Ch7_Assignments_Unwarranted_Assumption.md]]`
- **Створено концепції**:
  - `[[Помилки прийнятності]]`
  - `[[Помилки мовної плутанини]]`
  - `[[Помилки необґрунтованого припущення]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Атака на хибні міркування (Т. Е. Деймер) - Батч 8

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/attaking_json-segments/segment_071_Ch8_Missing_Evidence_Overview.md]]`
  - `[[Clippings/attaking_json-segments/segment_072_Ch8_38_Insufficient_Sample.md]]`
  - `[[Clippings/attaking_json-segments/segment_073_Ch8_39_Unrepresentative_Data.md]]`
  - `[[Clippings/attaking_json-segments/segment_074_Ch8_40_Arguing_from_Ignorance.md]]`
  - `[[Clippings/attaking_json-segments/segment_075_Ch8_41_Contrary_to_Fact_Hypothesis.md]]`
  - `[[Clippings/attaking_json-segments/segment_076_Ch8_42_Fallacy_of_Popular_Wisdom.md]]`
  - `[[Clippings/attaking_json-segments/segment_077_Ch8_43_Special_Pleading.md]]`
  - `[[Clippings/attaking_json-segments/segment_078_Ch8_44_Omission_of_Key_Evidence.md]]`
  - `[[Clippings/attaking_json-segments/segment_079_Ch8_Assignments_Missing_Evidence.md]]`
  - `[[Clippings/attaking_json-segments/segment_080_Ch8_Causal_Fallacies_Overview.md]]`
  - `[[Clippings/attaking_json-segments/segment_081_Ch8_45_Confusion_Necessary_Sufficient.md]]`
  - `[[Clippings/attaking_json-segments/segment_082_Ch8_46_Causal_Oversimplification.md]]`
  - `[[Clippings/attaking_json-segments/segment_083_Ch8_47_Post_Hoc_Fallacy.md]]`
  - `[[Clippings/attaking_json-segments/segment_084_Ch8_48_Confusion_of_Cause_and_Effect.md]]`
  - `[[Clippings/attaking_json-segments/segment_085_Ch8_49_Neglect_of_a_Common_Cause.md]]`
  - `[[Clippings/attaking_json-segments/segment_086_Ch8_50_Domino_Fallacy.md]]`
  - `[[Clippings/attaking_json-segments/segment_087_Ch8_51_Gamblers_Fallacy.md]]`
  - `[[Clippings/attaking_json-segments/segment_088_Ch8_Assignments_Causal_Fallacies.md]]`
- **Створено концепції**:
  - `[[Помилки достатності]]`
  - `[[Помилки браку доказів]]`
  - `[[Причинно-наслідкові помилки]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Атака на хибні міркування (Т. Е. Деймер) - Батч 9

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/attaking_json-segments/segment_089_Ch9_Counterevidence_Overview.md]]`
  - `[[Clippings/attaking_json-segments/segment_090_Ch9_52_Denying_the_Counterevidence.md]]`
  - `[[Clippings/attaking_json-segments/segment_091_Ch9_53_Ignoring_the_Counterevidence.md]]`
  - `[[Clippings/attaking_json-segments/segment_092_Ch9_Assignments_Counterevidence.md]]`
  - `[[Clippings/attaking_json-segments/segment_093_Ch9_Ad_Hominem_Overview.md]]`
  - `[[Clippings/attaking_json-segments/segment_094_Ch9_54_Abusive_Ad_Hominem.md]]`
  - `[[Clippings/attaking_json-segments/segment_095_Ch9_55_Poisoning_the_Well.md]]`
  - `[[Clippings/attaking_json-segments/segment_096_Ch9_56_Two_Wrongs_Fallacy.md]]`
  - `[[Clippings/attaking_json-segments/segment_097_Ch9_Assignments_Ad_Hominem.md]]`
  - `[[Clippings/attaking_json-segments/segment_098_Ch9_Diversion_Overview.md]]`
  - `[[Clippings/attaking_json-segments/segment_099_Ch9_57_Attacking_a_Straw_Man.md]]`
  - `[[Clippings/attaking_json-segments/segment_100_Ch9_58_Trivial_Objections.md]]`
  - `[[Clippings/attaking_json-segments/segment_101_Ch9_59_Red_Herring.md]]`
  - `[[Clippings/attaking_json-segments/segment_102_Ch9_60_Resort_to_Humor_or_Ridicule.md]]`
  - `[[Clippings/attaking_json-segments/segment_103_Ch9_Assignments_Diversion.md]]`
- **Створено концепції**:
  - `[[Помилки спростування]]`
  - `[[Уникання контрдоказів]]`
  - `[[Ad Hominem]]`
  - `[[Помилки відволікання]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Атака на хибні міркування (Т. Е. Деймер) - Батч 10

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/attaking_json-segments/segment_104_Ch10_Steps_in_Writing_Argumentative_Essay.md]]`
  - `[[Clippings/attaking_json-segments/segment_105_Ch10_Sample_Essay_Married_Woman_Name.md]]`
  - `[[Clippings/attaking_json-segments/segment_106_Ch10_Assignments.md]]`
  - `[[Clippings/attaking_json-segments/segment_107_Glossary_of_Fallacies.md]]`
  - `[[Clippings/attaking_json-segments/segment_108_Answers_to_Selected_Assignments.md]]`
  - `[[Clippings/attaking_json-segments/segment_109_Index.md]]`
- **Створено концепції**:
  - `[[Аргументативне есе]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Making Your Case (Scalia & Garner) - Батч 1

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/making_json_segments/segment_001_Title_Contents_Acknowledgments.md]]`
  - `[[Clippings/making_json_segments/segment_002_Foreword_by_Chief_Justice_John_G._Roberts_Jr..md]]`
  - `[[Clippings/making_json_segments/segment_003_Introduction.md]]`
  - `[[Clippings/making_json_segments/segment_004_Overview_-_General_Principles_of_Argumentation.md]]`
  - `[[Clippings/making_json_segments/segment_005_1._Be_sure_that_the_tribunal_has_jurisdiction..md]]`
  - `[[Clippings/making_json_segments/segment_006_2._Know_your_audience..md]]`
  - `[[Clippings/making_json_segments/segment_007_3._Know_your_case..md]]`
  - `[[Clippings/making_json_segments/segment_008_4._Know_your_adversary_s_case..md]]`
  - `[[Clippings/making_json_segments/segment_009_5._Pay_careful_attention_to_the_applicable_standard_of.md]]`
  - `[[Clippings/making_json_segments/segment_010_6._Never_overstate_your_case._Be_scrupulously_accurate..md]]`
  - `[[Clippings/making_json_segments/segment_011_7._If_possible_lead_with_your_strongest_argument..md]]`
  - `[[Clippings/making_json_segments/segment_012_8._If_you_re_the_first_to_argue_make_your_positive_case.md]]`
  - `[[Clippings/making_json_segments/segment_013_9._If_you_re_arguing_after_your_opponent_design_the_ord.md]]`
  - `[[Clippings/making_json_segments/segment_014_10._Occupy_the_most_defensible_terrain..md]]`
  - `[[Clippings/making_json_segments/segment_015_11._Yield_indefensible_terrain_ostentatiously..md]]`
  - `[[Clippings/making_json_segments/segment_016_12._Take_pains_to_select_your_best_arguments._Concentra.md]]`
  - `[[Clippings/making_json_segments/segment_017_13._Communicate_clearly_and_concisely..md]]`
  - `[[Clippings/making_json_segments/segment_018_14._Always_start_with_a_statement_of_the_main_issue_bef.md]]`
  - `[[Clippings/making_json_segments/segment_019_15._Appeal_not_just_to_rules_but_to_justice_and_common.md]]`
  - `[[Clippings/making_json_segments/segment_020_16._When_you_must_rely_on_fairness_to_modify_the_strict.md]]`
  - `[[Clippings/making_json_segments/segment_021_17._Understand_that_reason_is_paramount_with_judges_and.md]]`
  - `[[Clippings/making_json_segments/segment_022_18._Assume_a_posture_of_respectful_intellectual_equalit.md]]`
  - `[[Clippings/making_json_segments/segment_023_19._Restrain_your_emotions._And_don_t_accuse..md]]`
  - `[[Clippings/making_json_segments/segment_024_20._Control_the_semantic_playing_field..md]]`
  - `[[Clippings/making_json_segments/segment_025_21._Close_powerfully_and_say_explicitly_what_you_think.md]]`
- **Створено концепції**:
  - `[[Загальні принципи судової аргументації]]`
  - `[[Підготовка до судової аргументації]]`
  - `[[Стратегія та побудова аргументу]]`
  - `[[Етика та поведінка адвоката]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Making Your Case (Scalia & Garner) - Батч 2

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/making_json_segments/segment_026_Overview_-_Legal_Reasoning.md]]`
  - `[[Clippings/making_json_segments/segment_027_22._Think_syllogistically..md]]`
  - `[[Clippings/making_json_segments/segment_028_23._Know_the_rules_of_textual_interpretation..md]]`
  - `[[Clippings/making_json_segments/segment_029_24._In_cases_controlled_by_governing_legal_texts_always.md]]`
  - `[[Clippings/making_json_segments/segment_030_25._Be_prepared_to_defend_your_interpretation_by_resort.md]]`
  - `[[Clippings/making_json_segments/segment_031_26._Master_the_relative_weight_of_precedents..md]]`
  - `[[Clippings/making_json_segments/segment_032_27._Try_to_find_an_explicit_statement_of_your_major_pre.md]]`
- **Створено концепції**:
  - `[[Юридичне мислення]]`
  - `[[Силогістичне мислення в праві]]`
  - `[[Тлумачення юридичних текстів]]`
  - `[[Робота з прецедентами]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Making Your Case (Scalia & Garner) - Батч 3

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - Сегменти 033-060 (Правила 28-54) щодо підготовки briefs.
- **Створено концепції**:
  - `[[Підготовка процесуальних документів]]`
  - `[[Стиль юридичного письма]]`
  - `[[Оформлення та типографіка]]`
  - `[[Цитування авторитетів]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Making Your Case (Scalia & Garner) - Батч 4

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - Сегменти 061-090 (Правила 55-83) щодо усних дебатів (Oral Argument).
- **Створено концепції**:
  - `[[Значення та підготовка до усних дебатів]]`
  - `[[Стратегія усного виступу]]`
  - `[[Поведінка в залі суду]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Making Your Case (Scalia & Garner) - Батч 5

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - Сегменти 091-124 (Правила 84-115) щодо відповідей на запитання суддів та завершення справи.
- **Створено концепції**:
  - `[[Взаємодія із суддями]]`
  - `[[Робота з гіпотетичними ситуаціями]]`
  - `[[Завершення виступу та репутація]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Логічний аналіз юридичної аргументації (О. Щербина) - Батч 6 (Залишкові файли Розділу 5)

- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/scherbina_json_segments/segment_20_Розділ_5_5.1_Інтерпретація_як_спосіб_аргументування.md]]`
  - `[[Clippings/scherbina_json_segments/segment_21_Розділ_5_5.2_Логічна_складова_тлумачення_текстів.md]]`
  - `[[Clippings/scherbina_json_segments/segment_22_Розділ_5_5.3_Проблема_неясності_в_аргументації.md]]`
  - `[[Clippings/scherbina_json_segments/segment_23_Розділ_5_5.4_Визначення_кримінально_правової_норми.md]]`
  - `[[Clippings/scherbina_json_segments/segment_26_Список_використаної_літератури.md]]`
- **Створено концепції**:
  - `[[Тлумачення та неясність в аргументації]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Making Your Case (Scalia & Garner) - Батч 6 (Залишкові правила)
- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/making_json_segments/segment_033_Overview_-_Briefing.md]]`
  - `[[Clippings/making_json_segments/segment_034_28._Appreciate_the_objective_of_a_brief..md]]`
  - `[[Clippings/making_json_segments/segment_035_29._Strengthen_your_command_of_written_English..md]]`
  - `[[Clippings/making_json_segments/segment_036_30._Consult_the_applicable_rules_of_court..md]]`
  - `[[Clippings/making_json_segments/segment_037_31._Set_timelines_for_the_stages_of_your_work..md]]`
  - `[[Clippings/making_json_segments/segment_038_32._In_cooperation_with_your_opponent_prepare_the_Joint.md]]`
  - `[[Clippings/making_json_segments/segment_039_33._Spend_plenty_of_time_simply_getting_your_arguments..md]]`
  - `[[Clippings/making_json_segments/segment_040_34._Outline_your_brief.md]]`
  - `[[Clippings/making_json_segments/segment_041_35._Sit_down_and_write._Then_revise._Then_revise_again..md]]`
  - `[[Clippings/making_json_segments/segment_042_36._Know_how_to_use_and_arrange_the_parts_of_a_brief.md]]`
  - `[[Clippings/making_json_segments/segment_043_37._Advise_the_court_by_letter_of_significant_authority.md]]`
  - `[[Clippings/making_json_segments/segment_044_38._Learn_how_to_use_and_how_to_respond_to_amicus_brief.md]]`
  - `[[Clippings/making_json_segments/segment_045_39._Value_clarity_above_all_other_elements_of_style..md]]`
  - `[[Clippings/making_json_segments/segment_046_40._Use_captioned_section_headings..md]]`
  - `[[Clippings/making_json_segments/segment_047_41._Use_paragraphs_intelligently_signpost_your_argument.md]]`
  - `[[Clippings/making_json_segments/segment_048_42._To_clarify_abstract_concepts_give_examples..md]]`
  - `[[Clippings/making_json_segments/segment_049_43._Make_it_interesting..md]]`
  - `[[Clippings/making_json_segments/segment_050_44._Banish_jargon_hackneyed_expressions_and_needless_La.md]]`
  - `[[Clippings/making_json_segments/segment_051_45._Consider_using_contractions_occasionally_or_not..md]]`
  - `[[Clippings/making_json_segments/segment_052_46._Avoid_acronyms._Use_the_parties_names..md]]`
  - `[[Clippings/making_json_segments/segment_053_47._Don_t_overuse_italics_don_t_use_bold_type_except_in.md]]`
  - `[[Clippings/making_json_segments/segment_054_48._Describe_and_cite_authorities_with_scrupulous_accur.md]]`
  - `[[Clippings/making_json_segments/segment_055_49._Cite_authorities_sparingly..md]]`
  - `[[Clippings/making_json_segments/segment_056_50._Quote_authorities_more_sparingly_still..md]]`
  - `[[Clippings/making_json_segments/segment_057_51._Swear_off_substantive_footnotes_or_not..md]]`
  - `[[Clippings/making_json_segments/segment_058_52._Consider_putting_citations_in_footnotes_or_not..md]]`
  - `[[Clippings/making_json_segments/segment_059_53._Make_the_relevant_text_readily_available_to_the_cou.md]]`
  - `[[Clippings/making_json_segments/segment_060_54._Don_t_spoil_your_product_with_poor_typography..md]]`
  - `[[Clippings/making_json_segments/segment_061_Overview_-_Oral_Argument.md]]`
  - `[[Clippings/making_json_segments/segment_062_55._Appreciate_the_importance_of_oral_argument_and_know.md]]`
  - `[[Clippings/making_json_segments/segment_063_56._Prepare_yourself_generally_as_a_public_speaker..md]]`
  - `[[Clippings/making_json_segments/segment_064_57._Master_the_preferred_pronunciations_of_English_word.md]]`
  - `[[Clippings/making_json_segments/segment_065_58._Master_the_use_of_the_pause..md]]`
  - `[[Clippings/making_json_segments/segment_066_59._Send_up_the_skilled_advocate_most_knowledgeable_abo.md]]`
  - `[[Clippings/making_json_segments/segment_067_60._Avoid_splitting_the_argument_between_cocounsel..md]]`
  - `[[Clippings/making_json_segments/segment_068_61._Prepare_assiduously..md]]`
  - `[[Clippings/making_json_segments/segment_069_62._Learn_the_record..md]]`
  - `[[Clippings/making_json_segments/segment_070_63._Learn_the_cases..md]]`
  - `[[Clippings/making_json_segments/segment_071_64._Decide_which_parts_of_your_brief_you_ll_cover..md]]`
  - `[[Clippings/making_json_segments/segment_072_65._Be_flexible..md]]`
  - `[[Clippings/making_json_segments/segment_073_66._Be_absolutely_clear_on_the_theory_of_your_case..md]]`
  - `[[Clippings/making_json_segments/segment_074_67._Be_absolutely_clear_on_the_mandate_you_seek..md]]`
  - `[[Clippings/making_json_segments/segment_075_68._Organize_and_index_the_materials_you_may_need..md]]`
  - `[[Clippings/making_json_segments/segment_076_69._Conduct_moot_courts..md]]`
  - `[[Clippings/making_json_segments/segment_077_70._Watch_some_arguments..md]]`
  - `[[Clippings/making_json_segments/segment_078_71._On_the_eve_of_argument_check_your_authorities..md]]`
  - `[[Clippings/making_json_segments/segment_079_72._Arrive_at_court_plenty_early_with_everything_you_ne.md]]`
  - `[[Clippings/making_json_segments/segment_080_73._Make_a_good_first_impression._Dress_appropriately_a.md]]`
  - `[[Clippings/making_json_segments/segment_081_74._Seat_only_cocounsel_at_counsel_table..md]]`
  - `[[Clippings/making_json_segments/segment_082_75._Bear_in_mind_that_even_when_you_re_not_on_your_feet.md]]`
  - `[[Clippings/making_json_segments/segment_083_76._Approach_the_lectern_unencumbered_adjust_it_to_your.md]]`
  - `[[Clippings/making_json_segments/segment_084_77._Greet_the_court_and_if_necessary_introduce_yourself.md]]`
  - `[[Clippings/making_json_segments/segment_085_78._Have_your_opener_down_pat..md]]`
  - `[[Clippings/making_json_segments/segment_086_79._If_you_re_the_appellant_reserve_rebuttal_time..md]]`
  - `[[Clippings/making_json_segments/segment_087_80._Decide_whether_it_s_worth_giving_the_facts_and_hist.md]]`
  - `[[Clippings/making_json_segments/segment_088_81._If_you_re_the_appellant_lead_with_your_strength..md]]`
  - `[[Clippings/making_json_segments/segment_089_82._If_you_re_the_appellee_take_account_of_what_has_pre.md]]`
  - `[[Clippings/making_json_segments/segment_090_83._Avoid_detailed_discussion_of_precedents..md]]`
  - `[[Clippings/making_json_segments/segment_091_84._Focus_quickly_on_crucial_text_and_tell_the_court_wh.md]]`
  - `[[Clippings/making_json_segments/segment_092_85._Don_t_beat_a_dead_horse._Don_t_let_a_dead_horse_bea.md]]`
  - `[[Clippings/making_json_segments/segment_093_86._Stop_promptly_when_you_re_out_of_time..md]]`
  - `[[Clippings/making_json_segments/segment_094_87._When_you_have_time_left_but_nothing_else_useful_to.md]]`
  - `[[Clippings/making_json_segments/segment_095_88._Take_account_of_the_special_considerations_applicab.md]]`
  - `[[Clippings/making_json_segments/segment_096_89._Look_the_judges_in_the_eye._Connect..md]]`
  - `[[Clippings/making_json_segments/segment_097_90._Be_conversational_but_not_familiar..md]]`
  - `[[Clippings/making_json_segments/segment_098_91._Use_correct_courtroom_terminology..md]]`
  - `[[Clippings/making_json_segments/segment_099_92._Never_read_an_argument_never_deliver_it_from_memory.md]]`
  - `[[Clippings/making_json_segments/segment_100_93._Treasure_simplicity..md]]`
  - `[[Clippings/making_json_segments/segment_101_94._Don_t_chew_your_fingernails..md]]`
  - `[[Clippings/making_json_segments/segment_102_95._Present_your_argument_as_truth_not_as_your_opinion..md]]`
  - `[[Clippings/making_json_segments/segment_103_96._Never_speak_over_a_judge..md]]`
  - `[[Clippings/making_json_segments/segment_104_97._Never_ask_how_much_time_you_have_left..md]]`
  - `[[Clippings/making_json_segments/segment_105_98._Never_or_almost_never_put_any_other_question_to_the.md]]`
  - `[[Clippings/making_json_segments/segment_106_99._Be_cautious_about_humor..md]]`
  - `[[Clippings/making_json_segments/segment_107_100._Don_t_use_visual_aids_unintelligently..md]]`
  - `[[Clippings/making_json_segments/segment_108_101._Welcome_questions..md]]`
  - `[[Clippings/making_json_segments/segment_109_102._Listen_carefully_and_if_necessary_ask_for_clarific.md]]`
  - `[[Clippings/making_json_segments/segment_110_103._Never_postpone_an_answer..md]]`
  - `[[Clippings/making_json_segments/segment_111_104._If_you_don_t_know_say_so._And_never_give_a_categor.md]]`
  - `[[Clippings/making_json_segments/segment_112_105._Begin_with_a_yes_or_a_no..md]]`
  - `[[Clippings/making_json_segments/segment_113_106._Never_praise_a_question..md]]`
  - `[[Clippings/making_json_segments/segment_114_107._Willingly_answer_hypotheticals..md]]`
  - `[[Clippings/making_json_segments/segment_115_108._After_answering_transition_back_into_your_argument.md]]`
  - `[[Clippings/making_json_segments/segment_116_109._Recognize_friendly_questions..md]]`
  - `[[Clippings/making_json_segments/segment_117_110._Learn_how_to_handle_a_difficult_judge..md]]`
  - `[[Clippings/making_json_segments/segment_118_111._Beware_invited_concessions..md]]`
  - `[[Clippings/making_json_segments/segment_119_112._Advise_the_court_of_significant_new_authority..md]]`
  - `[[Clippings/making_json_segments/segment_120_113._If_you_re_unhappy_with_the_ruling_think_about_fili.md]]`
  - `[[Clippings/making_json_segments/segment_121_114._Learn_from_your_mistakes..md]]`
  - `[[Clippings/making_json_segments/segment_122_115._Plan_on_developing_a_reputation_for_excellence..md]]`
  - `[[Clippings/making_json_segments/segment_123_Sources_for_Inset_Quotations.md]]`
  - `[[Clippings/making_json_segments/segment_124_Recommended_Sources.md]]`
- **Створено концепції**:
  - `[[Додаткові правила судової аргументації]]`
- **Оновлено**: `[[index.md]]`

## [2026-09-13] ingest | Опрацювання логіки для юристів (В. Щербина) - Допоміжні матеріали
- **Дія**: Проведено інгістування (агентне).
- **Опрацьовано**:
  - `[[Clippings/logica_json_segments/segment_01_Титул_зміст.md]]`
  - `[[Clippings/logica_json_segments/segment_02_Передмова.md]]`
  - `[[Clippings/logica_json_segments/segment_08_Контрольні_питання_до_Розділу_1.md]]`
  - `[[Clippings/logica_json_segments/segment_14_Контрольні_питання_до_Розділу_2.md]]`
  - `[[Clippings/logica_json_segments/segment_20_Контрольні_питання_до_Розділу_3.md]]`
  - `[[Clippings/logica_json_segments/segment_26_Контрольні_питання_до_Розділу_4.md]]`
  - `[[Clippings/logica_json_segments/segment_31_Контрольні_питання_до_Розділу_5.md]]`
- **Створено концепції**: (немає, допоміжні матеріали)
- **Оновлено**: `[[index.md]]`


## [2026-09-14] ingest | Повна компіляція першоджерел Clippings у wiki/concepts

- **Дія**: Скомпільовано 311 розділів та сегментів із каталогу `Clippings/` у повноцінні статті `wiki/concepts/`.
- **Джерела**: 5 бібліотек першоджерел (`attaking_json-segments`, `making_json_segments`, `logica_json_segments`, `scherbina_json_segments`, `theory_json_segments`).
- **Результат**: Створено фронтматтери, виправлено артефакти розмітки, налаштовано зв'язки з батьківськими концептами та оновлено `index.md`.


## [2026-09-17] ingest | Компіляція першоджерела Дугласа Волтона (Informal Logic) за методом Karpathy LLM Wiki

- **Дія**: Скомпільовано 96 розділів та сегментів із каталогу `Clippings/douglas_json_segments` у повноцінні статті `wiki/concepts/`.
- **Джерело**: Дуглас Волтон, *«Informal Logic: A Pragmatic Approach»* (2nd Edition, Cambridge University Press).
- **Сутності**: Створено профіль автора `[[Дуглас Волтон (Douglas Walton)]]` у `wiki/entities/`.
- **Результат**: Сформовано YAML-фронтматтери (теги, дати, джерела, групи), налаштовано системні зв'язки з батьківськими концептами та оновлено центральний `index.md`.


## [2026-09-18] ingest | Компіляція першоджерела Ентоні Вестона (A Rulebook for Arguments) за методом Karpathy LLM Wiki

- **Дія**: Скомпільовано 73 розділів та сегментів із каталогу `Clippings/rulebook_json_segments` у повноцінні статті `wiki/concepts/`.
- **Джерело**: Ентоні Вестон, *«A Rulebook for Arguments»* (5th Edition, Hackett Publishing Company).
- **Сутності**: Створено профіль автора `[[Ентоні Вестон (Anthony Weston)]]` у `wiki/entities/`.
- **Результат**: Сформовано YAML-фронтматтери (теги, дати, джерела, групи), налаштовано системні зв'язки з батьківськими концептами та оновлено центральний `index.md`.
