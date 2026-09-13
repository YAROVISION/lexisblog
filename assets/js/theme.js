/**
 * Lexis Theme Manager
 * Supports: 'dark' (default/retro ocean van) and 'light' (soft monochrome minimalism)
 */
(function () {
  const STORAGE_KEY = 'lexis_theme';

  function getPreferredTheme() {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved === 'light' || saved === 'dark') {
      return saved;
    }
    // Default to dark theme matching original site
    return 'dark';
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    updateThemeButtons(theme);
  }

  function updateThemeButtons(theme) {
    const buttons = document.querySelectorAll('.theme-toggle-btn');
    buttons.forEach(btn => {
      const sunIcon = btn.querySelector('.icon-sun');
      const moonIcon = btn.querySelector('.icon-moon');
      const label = btn.querySelector('.theme-label');

      if (theme === 'light') {
        if (sunIcon) sunIcon.style.display = 'none';
        if (moonIcon) moonIcon.style.display = 'inline-block';
        if (label) label.textContent = 'Темна тема';
        btn.setAttribute('title', 'Увімкнути темну тему');
        btn.setAttribute('aria-label', 'Увімкнути темну тему');
      } else {
        if (sunIcon) sunIcon.style.display = 'inline-block';
        if (moonIcon) moonIcon.style.display = 'none';
        if (label) label.textContent = 'Світла тема';
        btn.setAttribute('title', 'Увімкнути світлу тему');
        btn.setAttribute('aria-label', 'Увімкнути світлу тему');
      }
    });
  }

  window.toggleTheme = function () {
    const current = document.documentElement.getAttribute('data-theme') || 'dark';
    const next = current === 'dark' ? 'light' : 'dark';
    localStorage.setItem(STORAGE_KEY, next);
    applyTheme(next);
  };

  // Immediate execution on load to prevent flash
  const initialTheme = getPreferredTheme();
  applyTheme(initialTheme);

  document.addEventListener('DOMContentLoaded', () => {
    updateThemeButtons(document.documentElement.getAttribute('data-theme') || 'dark');

    // Attach click handlers to any toggle buttons
    document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
      btn.addEventListener('click', e => {
        e.preventDefault();
        window.toggleTheme();
      });
    });
  });
})();
