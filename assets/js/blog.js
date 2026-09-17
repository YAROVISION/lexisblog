/**
 * Lexis Static Blog Module
 * Offline, standalone static database of articles with real-time category filtering and search
 */
const BLOG_POSTS = [
  {
    id: "judicial-error-formal-logic",
    slug: "anatomiya-sudovoyi-pomylky-formalna-logika",
    title: "Анатомія судової помилки: чому формальна логіка є головним захисником справедливості у кримінальному процесі",
    category: "Право",
    date: "2026-03-15",
    readTime: "5 хв",
    image: "assets/images/judicial-logic.jpg",
    summary: "Судове рішення не може базуватися на інтуїції. Порушення законів формальної логіки в українському судочинстві — це прямий процесуальний дефект, який веде до безумовного скасування судового акта.",
    content: `
      <p class="article-lead">
        Судове рішення в кримінальному провадженні не може базуватися на інтуїції чи суб'єктивних припущеннях. Будь-який вирок або ухвала — це передусім суворий акт раціонального мислення. Порушення законів формальної логіки в українському судочинстві є не просто абстрактною вадою викладу, а прямим процесуальним дефектом, який веде до безумовного скасування судового акта.
      </p>

      <h2>Буква закону: процесуальні вимоги до мислення</h2>
      <p>
        Кримінальний процесуальний кодекс України закріплює логічні стандарти як імперативні норми:
      </p>

      <ul class="legal-logic-list">
        <li>
          <span class="bullet">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">Законність, обґрунтованість і вмотивованість (ст. 370 КПК):</strong>
            <span>Рішення визнається обґрунтованим лише за дотримання закону достатньої підстави — коли факти підтверджені доказами. Вмотивованість вимагає чіткого логічного ланцюга: від посилок (досліджених матеріалів) до кінцевого висновку (кваліфікації дій).</span>
          </div>
        </li>
        <li>
          <span class="bullet">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">Оцінка доказів (ст. 94 КПК):</strong>
            <span>Оцінка кожного доказу окремо та всієї їх сукупності з точки зору достатності й взаємозв'язку є суто логічною операцією, що спирається на індукцію, дедукцію та усунення внутрішніх суперечностей.</span>
          </div>
        </li>
        <li>
          <span class="bullet">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">Стандарт «поза розумним сумнівом» (ст. 17 КПК):</strong>
            <span>Будь-яка непереборна логічна суперечність у версії сторони обвинувачення (порушення закону несуперечності) автоматично руйнує конструкцію підозри та тлумачиться на користь обвинуваченого.</span>
          </div>
        </li>
        <li>
          <span class="bullet">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">Право на справедливий суд (ст. 6 Конвенції з прав людини):</strong>
            <span>Практика ЄСПЛ («Серявін та інші проти України», «Проніна проти України») однозначно вказує: ігнорування судом ключових аргументів сторін або наявність висновків, які не випливають із фактів (помилка non sequitur), порушує конвенційні гарантії правосуддя.</span>
          </div>
        </li>
      </ul>

      <h2>Науковий вимір: силогізми, факти та ціна помилки</h2>
      <p>
        У теорії доказування судове рішення розглядається як класичний дедуктивний силогізм:
      </p>

      <div class="syllogism-box">
        <div class="syllogism-flow">
          <div class="syllogism-node major">
            <span class="syllogism-label">Велика посилка</span>
            <span class="syllogism-value">Норма права</span>
          </div>
          <span class="syllogism-op">+</span>
          <div class="syllogism-node minor">
            <span class="syllogism-label">Мала посилка</span>
            <span class="syllogism-value">Встановлені факти</span>
          </div>
          <span class="syllogism-op">&rarr;</span>
          <div class="syllogism-node conclusion">
            <span class="syllogism-label">Висновок</span>
            <span class="syllogism-value">Вирок</span>
          </div>
        </div>
      </div>

      <p>
        Якщо суд підміняє факти чи некоректно тлумачить диспозицію статті, уся конструкція руйнується, що за ст. 413 КПК кваліфікується як неправильне застосування закону про кримінальну відповідальність. Побудова обвинувачення на непрямих доказах також підпорядкована логічному методу виключення (Михайло Гродзінський, Вільям Твайнінг): якщо сукупність фактів допускає хоча б одну альтернативну версію події, теза залишається недоведеною.
      </p>

      <p>
        Чотири базові закони мислення — тотожності (незмінність предмета обвинувачення за ст. 337 КПК), несуперечності, виключеного третього та достатньої підстави (ст. 91 КПК) — слугують обов'язковими фільтрами. Їх ігнорування призводить до однобічності слідства та невідповідності висновків суду обставинам справи (ст. 409–411 КПК).
      </p>

      <h2>Бібліотека судового аналітика: що почитати для виявлення дефектів аргументації</h2>

      <h3>Юридична логіка та теорія судової аргументації</h3>
      <ul class="book-ref-list">
        <li class="book-ref-item">
          <span class="book-ref-bullet">⚬</span>
          <div>
            <a href="logica-textbook.html" class="book-ref-link">«Логіка для юристів» — Анатолій Конверський</a>
            <span class="book-ref-badge">В інтерактивному каталозі</span>
            <div style="margin-top: 0.25rem; color: var(--text-secondary); font-size: 0.95rem;">фундаментальний український підручник із розбором класичної логіки, проектованої на презумпції, докази та правові норми.</div>
          </div>
        </li>
        <li class="book-ref-item">
          <span class="book-ref-bullet">⚬</span>
          <div>
            <a href="making-your-case.html" class="book-ref-link">«Making Your Case: The Art of Persuading Judges» — Antonin Scalia, Bryan A. Garner</a>
            <span class="book-ref-badge">В інтерактивному каталозі</span>
            <div style="margin-top: 0.25rem; color: var(--text-secondary); font-size: 0.95rem;">практичне керівництво судді Верховного Суду США щодо побудови аргументів і пошуку логічних збоїв у судових актах.</div>
          </div>
        </li>
        <li class="book-ref-item">
          <span class="book-ref-bullet">⚬</span>
          <div>
            <a href="maccormick-theory.html" class="book-ref-link">«Legal Reasoning and Legal Theory» — Neil MacCormick</a>
            <span class="book-ref-badge">В інтерактивному каталозі</span>
            <div style="margin-top: 0.25rem; color: var(--text-secondary); font-size: 0.95rem;">фундаментальне дослідження дедуктивного обґрунтування та меж раціональності при судовому тлумаченні.</div>
          </div>
        </li>
        <li class="book-ref-item">
          <span class="book-ref-bullet">⚬</span>
          <div>
            <a href="scherbina-argumentation.html" class="book-ref-link">«Юридична аргументація: Логічні дослідження» — Олена Щербина</a>
            <span class="book-ref-badge">В інтерактивному каталозі</span>
            <div style="margin-top: 0.25rem; color: var(--text-secondary); font-size: 0.95rem;">монографія про сучасний логічний аналіз правових текстів і структуру судового діалогу.</div>
          </div>
        </li>
      </ul>

      <h3>Логічні помилки, софізми та критичний аналіз</h3>
      <ul class="book-ref-list">
        <li class="book-ref-item">
          <span class="book-ref-bullet">⚬</span>
          <div>
            <a href="damer-fallacies.html" class="book-ref-link">«Attacking Faulty Reasoning» — T. Edward Damer</a>
            <span class="book-ref-badge">В інтерактивному каталозі</span>
            <div style="margin-top: 0.25rem; color: var(--text-secondary); font-size: 0.95rem;">вичерпний довідник неформальних логічних помилок із готовими схемами побудови контраргументів.</div>
          </div>
        </li>
        <li class="book-ref-item">
          <span class="book-ref-bullet">⚬</span>
          <div>
            <strong style="color: var(--text-primary);">«Informal Logic: A Pragmatic Approach» — Douglas Walton:</strong>
            <div style="margin-top: 0.25rem; color: var(--text-secondary); font-size: 0.95rem;">робота провідного фахівця з виявлення маніпуляцій, упереджень і підміни тез у текстах.</div>
          </div>
        </li>
        <li class="book-ref-item">
          <span class="book-ref-bullet">⚬</span>
          <div>
            <strong style="color: var(--text-primary);">«A Rulebook for Arguments» — Anthony Weston:</strong>
            <div style="margin-top: 0.25rem; color: var(--text-secondary); font-size: 0.95rem;">стислий посібник для перевірки причинно-наслідкових зв’язків, аналогій та узагальнень.</div>
          </div>
        </li>
      </ul>

      <h3>Теорія доказів та прийняття рішень</h3>
      <ul class="book-ref-list">
        <li class="book-ref-item">
          <span class="book-ref-bullet">⚬</span>
          <div>
            <strong style="color: var(--text-primary);">«Evidence and Inference in the Law» — ред. Mike Redmayne, William Twining:</strong>
            <div style="margin-top: 0.25rem; color: var(--text-secondary); font-size: 0.95rem;">спеціалізована праця з логіки фактів, оцінки достатності доказів та усунення суперечностей у свідченнях.</div>
          </div>
        </li>
      </ul>
    `
  },
  {
    id: "english-16-lessons",
    slug: "angliyska-za-16-urokiv-interaktyvnyy-format",
    title: "Англійська за 16 уроків — тепер в інтерактивному форматі українською! 🇬🇧🇺🇦",
    category: "Навчання",
    date: "2026-03-11",
    readTime: "3 хв",
    image: "assets/images/english-lessons.jpg",
    summary: "Забудьте про нудне зубріння правил. Інтерактивна платформа вивчення англійської за 16 уроків: матриця дієслів 3×3, 78 000+ слів словника Балли, озвучення та гейміфікація на english.lexis.blog.",
    content: `
      <p class="article-lead">
        Забудьте про нудне зубріння правил. Головний принцип методики — спочатку подолати мовний бар'єр, а правильність прийде з практикою. Відтепер легендарна методика доступна в сучасному інтерактивному форматі з українським інтерфейсом!
      </p>

      <div class="article-cta-box" style="margin: 2rem 0; padding: 2.25rem 2rem; background: var(--bg-surface); border: 1px solid var(--accent-primary); border-radius: var(--border-radius-lg); box-shadow: 0 16px 40px rgba(0, 0, 0, 0.25); text-align: center;">
        <span style="font-size: 2.5rem; display: block; margin-bottom: 0.5rem;">🇬🇧 🇺🇦 🚀</span>
        <h3 style="font-size: 1.5rem; margin: 0 0 0.75rem; color: var(--text-primary); font-weight: 700;">Інтерактивний тренажер англійської мови</h3>
        <p style="color: var(--text-secondary); max-width: 620px; margin: 0 auto 1.5rem; font-size: 1.05rem; line-height: 1.6;">
          Почніть говорити вільно без страху помилок. 16 структурованих уроків, матриця часових форм та тренування вимови в один клік.
        </p>
        <a href="https://english.lexis.blog/" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="font-size: 1.05rem; padding: 0.85rem 2.25rem; display: inline-flex; align-items: center; gap: 0.5rem; text-decoration: none; font-weight: 600;">
          Почати навчання на english.lexis.blog &rarr;
        </a>
      </div>

      <h3>Що всередині застосунку:</h3>
      <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1.25rem; margin: 1.5rem 0 2.5rem;">
        <li style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem 1.4rem; background: rgba(0,0,0,0.03); border-radius: var(--border-radius-sm); border-left: 3px solid var(--accent-primary);">
          <span style="font-size: 1.3rem; line-height: 1;">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">16 адаптованих уроків</strong>
            <span style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Уся базова граматика, розкладена по поличках — від структури простого речення до складних модальних конструкцій без перевантаження термінами.</span>
          </div>
        </li>

        <li style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem 1.4rem; background: rgba(0,0,0,0.03); border-radius: var(--border-radius-sm); border-left: 3px solid var(--accent-primary);">
          <span style="font-size: 1.3rem; line-height: 1;">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">Матриця дієслів (3×3)</strong>
            <span style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Зручний візуальний тренажер для напрацювання автоматизму в часах (минулий, теперішній, майбутній × ствердження, заперечення, питання).</span>
          </div>
        </li>

        <li style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem 1.4rem; background: rgba(0,0,0,0.03); border-radius: var(--border-radius-sm); border-left: 3px solid var(--accent-primary);">
          <span style="font-size: 1.3rem; line-height: 1;">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">Інтерактивні тести</strong>
            <span style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Миттєвий зворотний зв'язок та детальні пояснення помилок українською мовою з порадами, як побудувати фразу природно.</span>
          </div>
        </li>

        <li style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem 1.4rem; background: rgba(0,0,0,0.03); border-radius: var(--border-radius-sm); border-left: 3px solid var(--accent-primary);">
          <span style="font-size: 1.3rem; line-height: 1;">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">Озвучення слів та фраз</strong>
            <span style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Нативна вимова кожної репліки в один клік — тренуйте сприйняття на слух та правильну інтонацію одночасно з читанням.</span>
          </div>
        </li>

        <li style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem 1.4rem; background: rgba(0,0,0,0.03); border-radius: var(--border-radius-sm); border-left: 3px solid var(--accent-primary);">
          <span style="font-size: 1.3rem; line-height: 1;">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">Словник на 78 000+ слів</strong>
            <span style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Фундаментальна академічна лексикографічна база М. І. Балли з транскрипцією, прикладами вживання та вбудованим мінітренажером слів.</span>
          </div>
        </li>

        <li style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem 1.4rem; background: rgba(0,0,0,0.03); border-radius: var(--border-radius-sm); border-left: 3px solid var(--accent-primary);">
          <span style="font-size: 1.3rem; line-height: 1;">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">Гейміфікація та збереження прогресу</strong>
            <span style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Заробляйте XP за кожну правильну відповідь, тримайте щоденний вогняний стрик та відстежуйте власний рівень володіння мовою без жодної обов'язкової реєстрації.</span>
          </div>
        </li>
      </ul>

      <h3>Подолайте мовний бар'єр вже сьогодні</h3>
      <p>
        Коли граматичні форми перетворюються на рефлекс, страх говорити зникає сам по собі. Застосунок оптимізовано як для комп'ютерів, так і для смартфонів — займайтеся по 10–15 хвилин на день у комфортному для вас темпі.
      </p>

      <div style="margin-top: 2.5rem; padding: 1.75rem; border-radius: var(--border-radius-md); background: rgba(0, 194, 168, 0.06); border: 1px dashed var(--accent-primary); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
        <div>
          <span style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); display: block; margin-bottom: 0.25rem;">Працює прямо в браузері без завантажень!</span>
          <span style="color: var(--text-secondary); font-size: 0.95rem;">Переходьте за посиланням та починайте говорити англійською:</span>
        </div>
        <a href="https://english.lexis.blog/" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="text-decoration: none;">
          🚀 english.lexis.blog &rarr;
        </a>
      </div>
    `
  },
  {
    id: "tricks-communication-defense",
    slug: "100-tryukiv-u-spilkuvanni-manipulyatsiyi-ta-zakhyst",
    title: "100 Трюків у Спілкуванні: Психологічні Маніпуляції та Захист 🧠🛡️",
    category: "Психологія",
    date: "2026-03-11",
    readTime: "4 хв",
    image: "assets/images/tricks-defense.jpg",
    summary: "Як розпізнати прихований тиск, знецінення чи маніпуляції в переговорах та щоденних розмовах? Запустили інтерактивну онлайн-енциклопедію психологічного самозахисту за матеріалами книги П. Ф. Ліонова на tricks.lexis.blog.",
    content: `
      <p class="article-lead">
        Як розпізнати прихований тиск, знецінення чи маніпуляції в переговорах та щоденних розмовах? Команда платформи Lexis запустила інтерактивну онлайн-енциклопедію психологічного самозахисту за матеріалами книги П. Ф. Ліонова.
      </p>

      <div class="article-cta-box" style="margin: 2rem 0; padding: 2.25rem 2rem; background: var(--bg-surface); border: 1px solid var(--accent-primary); border-radius: var(--border-radius-lg); box-shadow: 0 16px 40px rgba(0, 0, 0, 0.25); text-align: center;">
        <span style="font-size: 2.5rem; display: block; margin-bottom: 0.5rem;">🧠 🛡️</span>
        <h3 style="font-size: 1.5rem; margin: 0 0 0.75rem; color: var(--text-primary); font-weight: 700;">Інтерактивна енциклопедія психологічного самозахисту</h3>
        <p style="color: var(--text-secondary); max-width: 620px; margin: 0 auto 1.5rem; font-size: 1.05rem; line-height: 1.6;">
          100 розібраних маніпулятивних прийомів, софізмів та готових вербальних щитів для захисту власного психологічного простору.
        </p>
        <a href="https://tricks.lexis.blog/" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="font-size: 1.05rem; padding: 0.85rem 2.25rem; display: inline-flex; align-items: center; gap: 0.5rem; text-decoration: none; font-weight: 600;">
          Досліджуйте онлайн: tricks.lexis.blog &rarr;
        </a>
      </div>

      <h3>Ключові можливості онлайн-енциклопедії:</h3>
      <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1.25rem; margin: 1.5rem 0 2.5rem;">
        <li style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem 1.4rem; background: rgba(0,0,0,0.03); border-radius: var(--border-radius-sm); border-left: 3px solid var(--accent-primary);">
          <span style="font-size: 1.3rem; line-height: 1;">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">100 розібраних трюків</strong>
            <span style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Від мови тіла та логічних софізмів до трансакційних ігор і класичних стратагем. Кожен трюк розібрано за структурою: як діє, чому спрацьовує та чим небезпечний.</span>
          </div>
        </li>

        <li style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem 1.4rem; background: rgba(0,0,0,0.03); border-radius: var(--border-radius-sm); border-left: 3px solid var(--accent-primary);">
          <span style="font-size: 1.3rem; line-height: 1;">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">10 тематичних категорій</strong>
            <span style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Страх, провина, атаки на статус, блеф, альтернативні пастки, лестощі, фальшива авторитетність, розмивання відповідальності та пасивна агресія.</span>
          </div>
        </li>

        <li style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem 1.4rem; background: rgba(0,0,0,0.03); border-radius: var(--border-radius-sm); border-left: 3px solid var(--accent-primary);">
          <span style="font-size: 1.3rem; line-height: 1;">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">Тренажер рефлексів</strong>
            <span style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Інтерактивні змодельовані кейси з практичними запитаннями та готовими сценаріями для миттєвої контратаки й повернення контролю над розмовою.</span>
          </div>
        </li>

        <li style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem 1.4rem; background: rgba(0,0,0,0.03); border-radius: var(--border-radius-sm); border-left: 3px solid var(--accent-primary);">
          <span style="font-size: 1.3rem; line-height: 1;">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">Миттєвий пошук та фільтри</strong>
            <span style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Зручна фільтрація за контекстом спілкування та рівнями небезпеки від легкого (побутового) до критичного (деструктивного).</span>
          </div>
        </li>

        <li style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem 1.4rem; background: rgba(0,0,0,0.03); border-radius: var(--border-radius-sm); border-left: 3px solid var(--accent-primary);">
          <span style="font-size: 1.3rem; line-height: 1;">⚬</span>
          <div>
            <strong style="color: var(--text-primary); display: block; font-size: 1.05rem; margin-bottom: 0.25rem;">Практичні фрази захисту</strong>
            <span style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Копіювання дієвих контрударів, деескалаційних відповідей та вербальних бар'єрів в один клік для швидкого застосування.</span>
          </div>
        </li>
      </ul>

      <h3>Мистецтво виявлення прихованого тиску</h3>
      <p>
        У ділових переговорах, публічних дискусіях та навіть дружніх бесідах найнебезпечніші маніпуляції зазвичай не виглядають як відкрита агресія. Вони діють тонко: через розхитування впевненості, нав'язування чужих зобов'язань чи спотворення фактів. Енциклопедія за книгою П. Ф. Ліонова покликана перетворити інтуїтивне відчуття дискомфорту на чітке розуміння прийому, який застосовують проти вас, та дати вивірений інструмент захисту.
      </p>

      <div style="margin-top: 2.5rem; padding: 1.75rem; border-radius: var(--border-radius-md); background: rgba(26, 107, 255, 0.05); border: 1px dashed var(--accent-primary); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
        <div>
          <span style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); display: block; margin-bottom: 0.25rem;">Готові прокачати комунікативний імунітет?</span>
          <span style="color: var(--text-secondary); font-size: 0.95rem;">Досліджуйте повну інтерактивну базу прийомів онлайн:</span>
        </div>
        <a href="https://tricks.lexis.blog/" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="text-decoration: none;">
          🔗 tricks.lexis.blog &rarr;
        </a>
      </div>
    `
  },
  {
    id: "knowledge-universe",
    slug: "znannya-yak-vsesvit-sproba-struktuvannya",
    title: "Знання як Всесвіт: спроба структурування",
    category: "Лінгвістика",
    date: "2026-03-11",
    readTime: "5 хв",
    image: "assets/images/knowledge-universe.jpg",
    summary: "Знання Всесвіту неосяжні, а слова — це капсули досвіду. Як розподіл понять на 10 категорій абстракції накладає координатну сітку на хаос людського пізнання?",
    content: `
      <p>Знання Всесвіту неосяжні. Якщо уявити всю сукупність людського пізнання у вигляді космосу, то відома нам його частина виглядатиме як зоряне небо — величезна, але все ж лише мала частка того, що існує насправді. Людство протягом своєї еволюції здобувало ці знання і зберігало їх у особливих контейнерах — словах. Саме слово є одиницею збереження та передачі смислу, капсулою досвіду, що переживає покоління.</p>

      <p>Ці знання створювались хаотично — залежно від нагальних обставин, практичних потреб, людського ентузіазму, наукового прогресу та простого прагнення гідно жити. Саме тому структурувати їх надзвичайно важко: вони не мають єдиного автора, єдиного плану, єдиної логіки виникнення.</p>

      <h3>Полюс граничної абстракції та полюс чуттєвого досвіду</h3>
      <p>Проте існує підхід, що дозволяє впорядкувати цей хаос. Він полягає у розподілі всіх слів за ступенем абстракції.</p>

      <p>На одному полюсі цього спектру знаходяться слова найвищого рівня абстракції — такі як <em>буття, Всесвіт, свідомість, нескінченність</em>. Дати їм вичерпне визначення практично неможливо: ці поняття настільки грандіозні, що будь-яке формулювання лише окреслює їх межі, але не вміщає повністю.</p>

      <p>На протилежному полюсі — слова максимально конкретні: назви кольорів, тактильних відчуттів, смаків. Наприклад, <em>зелений</em> або <em>червоний</em>. Парадокс полягає в тому, що ці поняття також не піддаються словесному опису — але з протилежної причини: вони надто безпосередні, надто чуттєві. Як пояснити зелений колір людині, яка ніколи його не бачила? Жодне слово тут не допоможе — лише прямий досвід.</p>

      <p>Таким чином, обидва полюси — граничне абстрактне і граничне конкретне — виявляються однаково невимовними. Мова найкраще працює в просторі між ними.</p>

      <h3>10 категорій абстракції як координатна сітка</h3>
      <p>Спираючись саме на цю ідею, слова були розподілені на 10 категорій абстракції, що утворюють чітку ієрархічну структуру:</p>
      <ul>
        <li><strong>На вершині (1 категорія):</strong> «Філософські поняття» — слова, що охоплюють найзагальніші закономірності існування.</li>
        <li><strong>В основі (10 категорія):</strong> «Максимально конкретні поняття» — слова, прив'язані до безпосереднього чуттєвого досвіду.</li>
      </ul>

      <p>Така класифікація — це не лише інструмент систематизації мови. Це спроба накласти на безмежний океан людського знання координатну сітку, яка допомагає орієнтуватися: розуміти, на якому рівні абстракції ведеться розмова, де знаходиться та чи інша ідея у загальній картині світу, і як різні поняття співвідносяться між собою.</p>
    `
  },
  {
    id: "sherlock",
    slug: "sherlock-holmes-nam-ne-dopomozhe",
    title: "Шерлок Холмс нам не допоможе",
    category: "Лінгвістика",
    date: "2026-03-11",
    readTime: "4 хв",
    image: "assets/images/sherlock.jpg",
    summary: "Усі ми захоплювалися дедуктивним методом Шерлока Холмса. Але коли йдеться про долю людини під слідством чи в суді — чи достатньо лише життєвого досвіду та інтуїтивного «давай міркувати логічно»?",
    content: `
      <p>Усі ми дивилися фільми й читали книги про Шерлока Холмса і, звісно, захоплювалися його здатністю розплутувати складні ситуації за допомогою славнозвісного дедуктивного методу. Хто з нас не мріяв стати таким само проникливим?</p>

      <p>За аналогією з цим персонажем у людей склалося стійке враження, що під час розслідування слідчі так само послуговуються якимись особливими логічними здібностями і з легкістю розкривають найзаплутаніші злочини. Однак у реальному житті все виглядає інакше — так само, як ніколи не існував сам Шерлок Холмс. Дедуктивний метод, формальна логіка, блискучі умовиводи — усі ці образи, засвоєні нами ще в дитинстві, непомітно формують переконання, що й доросле життя влаштоване так само.</p>

      <h3>Чи знаємо ми закони логіки?</h3>
      <p>Саме тому заклик «Давай міркувати логічно!» під час суперечки звучить дещо курйозно, якщо поставити зустрічне запитання: «А які закони логіки ти знаєш?». Мало хто здатен на нього відповісти. Мало хто навіть скаже, скільки таких законів існує. Здавалося б, усе це свідчить про нашу нездатність мислити логічно.</p>

      <p>Але парадокс полягає в іншому: кожен із нас здатен до логічного мислення — і без жодної спеціальної освіти. Накопичений життєвий досвід забезпечує нас достатніми інструментами й знаннями, аби вирішувати повсякденні задачі, планувати, встановлювати причини тих чи інших подій, розставляти пріоритети. І з цим ми справляємося цілком успішно.</p>

      <h3>Ціна помилки у вирішенні людських доль</h3>
      <p>Але коли йдеться про долю людини, яка перебуває під слідством, про майнові суперечки в суді чи про трудові конфлікти — чи достатньо нам одного лише життєвого досвіду? Чи можна покладатися на інтуїтивне «давай міркувати логічно»? Мабуть, у таких ситуаціях ми прагнемо чогось надійнішого. Ми хочемо, щоб людина, яка вирішує чиюсь долю, справді знала закони логіки і вміла їх застосовувати.</p>

      <p>У світі багато розумних і відповідальних людей. Але навіщо покладатися на випадок, якщо можна отримати достовірну відповідь — саме для цього і створена наша програма.</p>
    `
  },
  {
    id: "1",
    slug: "ai-in-legal-analysis",
    title: "Штучний інтелект у судовому аналізі документів: можливості та межі",
    category: "Технології",
    date: "2026-03-08",
    readTime: "5 хв",
    image: "assets/images/professional-headshot-1.png",
    summary: "Як сучасні LLM моделі та семантичні графи допомагають юристам виявляти логічні прогалини у процесуальних документах та перевіряти відповідність практиці Верховного Суду.",
    content: `
      <h2>Революція юридичного аналізу даних</h2>
      <p>Юридична практика завжди вимагала надзвичайної уваги до кожної коми, формулювання та прецеденту. З появою спеціалізованих мовних моделей аналіз обвинувальних актів чи судових рішень переходить на абсолютно новий рівень.</p>
      
      <h3>Де ШІ найбільш ефективний?</h3>
      <p>Сучасні алгоритми здатні за лічені секунди вирішувати завдання, які раніше забирали години монотонної праці:</p>
      <ul>
        <li><strong>Перевірка обов'язкових реквізитів:</strong> автоматичний аудит структури документа відповідно до КПК України.</li>
        <li><strong>Пошук внутрішніх протиріч:</strong> виявлення випадків, коли висновки в мотивувальній частині не узгоджуються з викладеними доказами.</li>
        <li><strong>Зіставлення з практикою ЄСПЛ:</strong> миттєвий пошук рішень Європейського суду за схожими обставинами справи.</li>
      </ul>

      <h3>Чому фінальне слово завжди за правником?</h3>
      <p>Незважаючи на потужність штучного інтелекту, оцінка справедливості, контексту людських взаємин та етичної складової залишається виключно людською прерогативою. ШІ в системі Lexis слугує підсилювачем аналітичних здібностей спеціаліста, мінімізуючи ризик людської неуважності.</p>
    `
  },
  {
    id: "2",
    slug: "abstraction-ladder-logic",
    title: "Шкала абстракції понять: як точність слів впливає на юридичну силу тексту",
    category: "Лінгвістика",
    date: "2026-03-01",
    readTime: "4 хв",
    image: "assets/images/professional-headshot-2.jpg",
    summary: "Чому розмиті категорії послаблюють доказову базу і яким чином рівень конкретизації іменників визначає однозначність судового рішення.",
    content: `
      <h2>Драбина абстракцій Хаякави</h2>
      <p>Відомий лінгвіст Семюел Хаякава запропонував концепцію «драбини абстракцій», яка ідеально пояснює природу юридичної визначеності. На найнижчому щаблі знаходяться фізичні конкретні об'єкти, а на найвищому — загальні абстрактні поняття на кшталт «справедливість» чи «суспільне благо».</p>

      <h3>Принцип визначеності в праві</h3>
      <p>Юридичний документ має силу лише тоді, коли використовувані терміни не залишають простору для двозначного тлумачення. Якщо в тексті договору замість «доставити вантаж масою 500 кг за адресою...» написати «здійснити перевезення майна у прийнятний строк», виникає небезпечна правова невизначеність.</p>

      <h3>Рівні абстракції в алгоритмах Lexis</h3>
      <p>Наш словниковий рушій маркує слова за шкалою від 1 до 10. Нижчий рівень гарантує конкретику, тоді як високий рівень позначає узагальнення. Баланс цих рівнів у процесуальному документі — запорука його логічної бездоганності.</p>
    `
  },
  {
    id: "3",
    slug: "logical-fallacies-in-contracts",
    title: "5 типових логічних помилок у юридичних висновках та договорах",
    category: "Навчання",
    date: "2026-02-24",
    readTime: "6 хв",
    image: "assets/images/professional-headshot-3.png",
    summary: "Підміна понять, коло в доведенні, хибна дилема та інші підводні камені, які руйнують правову позицію сторін у судовому розгляді.",
    content: `
      <h2>Логіка як фундамент судового процесу</h2>
      <p>Навіть бездоганне знання нормативної бази не врятує позицію, якщо аргументація побудована на логічній хибі. Розглянемо п'ять найпоширеніших помилок, які фіксуються в практиці.</p>

      <h3>1. Circulus in demonstrando (Коло в доведенні)</h3>
      <p>Ситуація, коли теза доводиться за допомогою аргументу, який сам базується на істинності цієї тези. Наприклад: «Діяння є неправомірним, оскільки особа вчинила протиправний вчинок».</p>

      <h3>2. Підміна поняття (Equivocation)</h3>
      <p>Використання одного й того ж терміна у двох різних значеннях упродовж одного висновку. В юридичній термінології це неприпустимо, оскільки закон чітко визначає дефініцію кожного інституту.</p>

      <h3>3. Недостатня підстава</h3>
      <p>Коли висновок про винуватість або обставини справи робиться на основі припущень або одиничного факту, що не виключає інших версій.</p>
    `
  },
  {
    id: "4",
    slug: "lexis-major-update-semantic-graphs",
    title: "Велике оновлення платформи Lexis: семантичний графовий аналіз",
    category: "Новини",
    date: "2026-02-18",
    readTime: "3 хв",
    image: "assets/images/professional-headshot-4.jpg",
    summary: "Презентація оновленої системи візуалізації зв'язків між поняттями, швидкого локального пошуку та глибокої підтримки морфології.",
    content: `
      <h2>Новий етап розвитку Lexis</h2>
      <p>Ми раді представити масштабне оновлення ядра Lexis. Відтепер дослідження української мови та аналіз текстових масивів стає ще наочнішим та швидшим.</p>

      <h3>Що нового в цій версії:</h3>
      <ul>
        <li><strong>Семантичні зв'язки нового покоління:</strong> миттєва побудова ланцюгів «гіперонім — гіпонім» для понад 250 000 слів українського словника.</li>
        <li><strong>Автономність та швидкість:</strong> повна статична оптимізація інтерфейсу без затримок мережі.</li>
        <li><strong>Оновлений дизайн:</strong> підтримка світлої мінімалістичної та темної контрастної палітр.</li>
      </ul>
    `
  },
  {
    id: "5",
    slug: "hyponyms-hypernyms-language-architecture",
    title: "Гіпоніми та гіпероніми: як класифікація слів будує логіку мови",
    category: "Лінгвістика",
    date: "2026-02-10",
    readTime: "4 хв",
    image: "assets/images/professional-headshot-5.jpg",
    summary: "Як ієрархічні відношення роду й виду формують каркас української лексики і чому це критично для автоматизованої обробки мови.",
    content: `
      <h2>Ієрархія смислів</h2>
      <p>Гіперонім — це ширше, родове поняття (наприклад, «правочин»), а гіпонім — вужче, видове («договір купівлі-продажу», «заповіт»). Розуміння цих зв'язків дозволяє штучному інтелекту не просто рахувати частотність слів, а осмислювати їхню ієрархію.</p>

      <p>Українська мова має одну з найбагатших систем словотвору та семантичної градації у світі. Правильна класифікація слів дозволяє створювати надійні онтології для баз знань та інтелектуальних пошукових систем.</p>
    `
  }
];

// Formatting helper for Ukrainian dates
function formatDateUa(dateStr) {
  const options = { day: 'numeric', month: 'long', year: 'numeric' };
  return new Date(dateStr).toLocaleDateString('uk-UA', options);
}

// Blog list controller
function initBlogList() {
  const postsGrid = document.getElementById('blog-posts-grid');
  const searchInput = document.getElementById('blog-search');
  const categoryPills = document.querySelectorAll('.pill-btn');

  if (!postsGrid) return;

  let currentCategory = 'Всі';
  let searchQuery = '';

  function renderPosts() {
    const filtered = BLOG_POSTS.filter(post => {
      const matchCat = currentCategory === 'Всі' || post.category === currentCategory;
      const matchSearch = post.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          post.summary.toLowerCase().includes(searchQuery.toLowerCase());
      return matchCat && matchSearch;
    });

    if (filtered.length === 0) {
      postsGrid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 4rem 1rem;">
          <p style="color: var(--text-muted); font-size: 1.25rem; margin-bottom: 1.5rem;">Статей не знайдено за вашим запитом.</p>
          <button class="btn btn-secondary" onclick="resetFilters()">Скинути всі фільтри</button>
        </div>
      `;
      return;
    }

    postsGrid.innerHTML = filtered.map(post => `
      <article class="post-card">
        <div class="post-img-box">
          <img src="${post.image}" alt="${post.title}" loading="lazy">
          <span class="post-cat-badge">${post.category}</span>
        </div>
        <div class="post-body">
          <div class="post-meta">
            <span>📅 ${formatDateUa(post.date)}</span>
            <span>⏱ ${post.readTime}</span>
          </div>
          <h3 class="post-title">${post.title}</h3>
          <p class="post-summary">${post.summary}</p>
          <div>
            <a href="blog-post.html?slug=${post.slug}" class="post-read-more">
              Читати далі &rarr;
            </a>
          </div>
        </div>
      </article>
    `).join('');
  }

  window.resetFilters = function() {
    currentCategory = 'Всі';
    searchQuery = '';
    if (searchInput) searchInput.value = '';
    categoryPills.forEach(p => p.classList.toggle('active', p.dataset.category === 'Всі'));
    renderPosts();
  };

  categoryPills.forEach(pill => {
    pill.addEventListener('click', () => {
      categoryPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      currentCategory = pill.dataset.category;
      renderPosts();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.trim();
      renderPosts();
    });
  }

  renderPosts();
}

// Single article reader controller
function initArticleReader() {
  const articleContainer = document.getElementById('single-article-content');
  if (!articleContainer) return;

  const urlParams = new URLSearchParams(window.location.search);
  const slug = urlParams.get('slug') || BLOG_POSTS[0].slug;
  const post = BLOG_POSTS.find(p => p.slug === slug) || BLOG_POSTS[0];

  document.title = `${post.title} | Lexis Blog`;

  const metaEl = document.getElementById('article-meta');
  const titleEl = document.getElementById('article-title');
  const catEl = document.getElementById('article-category');
  const imgEl = document.getElementById('article-image');

  if (catEl) catEl.textContent = post.category;
  if (metaEl) metaEl.innerHTML = `<span>📅 ${formatDateUa(post.date)}</span> • <span>⏱ ${post.readTime} читання</span>`;
  if (titleEl) titleEl.textContent = post.title;
  if (imgEl) {
    imgEl.src = post.image;
    imgEl.alt = post.title;
  }

  articleContainer.innerHTML = post.content;
}

document.addEventListener('DOMContentLoaded', () => {
  initBlogList();
  initArticleReader();
});
