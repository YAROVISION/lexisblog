/**
 * Т. Едвард Деймер - Атака на хибні міркування: Практичний посібник з безпомилкової аргументації
 * Інтерактивний рідер, зміст та повнотекстовий пошук
 * Vanilla JS
 */

document.addEventListener('DOMContentLoaded', () => {
  const bookData = window.DAMER_DATA;
  if (!bookData || !bookData.segments) {
    console.error('Дані книги Т. Едварда Деймера не завантажено.');
    return;
  }

  // DOM Elements
  const searchInput = document.getElementById('segment-search-input');
  const searchClearBtn = document.getElementById('search-clear-btn');
  const searchStats = document.getElementById('search-stats');
  const sectionFilterContainer = document.getElementById('section-filters');
  const tocContainer = document.getElementById('book-toc-container');
  const searchResultsContainer = document.getElementById('search-results-container');
  const tocViewSection = document.getElementById('toc-view-section');
  const searchViewSection = document.getElementById('search-view-section');
  
  // Modal / Reader elements
  const readerModal = document.getElementById('segment-reader-modal');
  const modalCloseBtn = document.getElementById('modal-close-btn');
  const modalSectionTitle = document.getElementById('modal-section-title');
  const modalSegmentTitle = document.getElementById('modal-segment-title');
  const modalSegmentMeta = document.getElementById('modal-segment-meta');
  const modalSegmentBody = document.getElementById('modal-segment-body');
  const modalPrevBtn = document.getElementById('modal-prev-btn');
  const modalNextBtn = document.getElementById('modal-next-btn');
  const modalCopyBtn = document.getElementById('modal-copy-btn');
  const copyToast = document.getElementById('copy-toast');

  let currentSegmentId = 1;
  let activeSectionFilter = 'all';
  let searchQuery = '';

  // 1. Initialize Section Filters
  function initSectionFilters() {
    if (!sectionFilterContainer) return;
    sectionFilterContainer.innerHTML = '';
    
    const allBtn = document.createElement('button');
    allBtn.className = 'filter-chip active';
    allBtn.dataset.section = 'all';
    allBtn.textContent = 'Усі розділи (' + bookData.segments.length + ')';
    allBtn.addEventListener('click', () => setSectionFilter('all'));
    sectionFilterContainer.appendChild(allBtn);

    bookData.sections.forEach(sec => {
      const count = bookData.segments.filter(s => s.section === sec).length;
      if (count === 0) return;
      const btn = document.createElement('button');
      btn.className = 'filter-chip';
      btn.dataset.section = sec;
      
      btn.textContent = `${sec} (${count})`;
      btn.title = sec;
      btn.addEventListener('click', () => setSectionFilter(sec));
      sectionFilterContainer.appendChild(btn);
    });
  }

  function setSectionFilter(sectionName) {
    activeSectionFilter = sectionName;
    document.querySelectorAll('#section-filters .filter-chip').forEach(chip => {
      chip.classList.toggle('active', chip.dataset.section === sectionName);
    });
    renderTOC();
    if (searchQuery.trim() !== '') {
      performSearch();
    }
  }

  // 2. Render Table of Contents (Grouped by Sections in Bento Cards)
  function renderTOC() {
    if (!tocContainer) return;
    tocContainer.innerHTML = '';

    const sectionsToRender = activeSectionFilter === 'all'
      ? bookData.sections
      : [activeSectionFilter];

    sectionsToRender.forEach(sec => {
      const segs = bookData.segments.filter(s => s.section === sec);
      if (segs.length === 0) return;

      const secCard = document.createElement('div');
      secCard.className = 'bento-card toc-section-card';

      const secHeader = document.createElement('div');
      secHeader.className = 'toc-section-header';
      secHeader.innerHTML = `
        <div class="toc-sec-title-wrap">
          <span class="toc-sec-badge">${segs.length} ${pluralizeSegments(segs.length)}</span>
          <h2 class="toc-section-title">${escapeHTML(sec)}</h2>
        </div>
      `;

      const list = document.createElement('div');
      list.className = 'toc-segment-list';

      segs.forEach(seg => {
        const item = document.createElement('div');
        item.className = 'toc-segment-item';
        item.id = `toc-seg-${seg.id}`;

        const pageLabel = seg.pages_label ? `с. ${seg.pages_label}` : `${seg.pages} стор.`;
        const subBadge = seg.subsegments && seg.subsegments.length > 1
          ? ` • ${seg.subsegments.length} підрозділів`
          : '';

        item.innerHTML = `
          <div class="toc-item-left">
            <span class="seg-number">#${seg.id}</span>
            <div class="seg-info">
              <span class="seg-title">${escapeHTML(seg.title)}</span>
              <span class="seg-meta">${pageLabel} • ${formatWordCount(seg.text)} ${subBadge}</span>
            </div>
          </div>
          <button class="btn-read-segment" data-id="${seg.id}" aria-label="Читати сегмент ${seg.id}">
            Читати &rarr;
          </button>
        `;

        item.addEventListener('click', () => {
          openReader(seg.id);
        });

        list.appendChild(item);
      });

      secCard.appendChild(secHeader);
      secCard.appendChild(list);
      tocContainer.appendChild(secCard);
    });
  }

  // 3. Perform Fast Search Across Segments
  function performSearch() {
    const q = searchQuery.trim().toLowerCase();
    
    if (q === '') {
      tocViewSection.style.display = 'block';
      searchViewSection.style.display = 'none';
      if (searchClearBtn) searchClearBtn.style.display = 'none';
      searchStats.textContent = `Всього ${bookData.segments.length} сегментів книги (60 софізмів та логічних помилок)`;
      return;
    }

    if (searchClearBtn) searchClearBtn.style.display = 'block';
    tocViewSection.style.display = 'none';
    searchViewSection.style.display = 'block';

    const terms = q.split(/\s+/).filter(t => t.length > 1);
    if (terms.length === 0) {
      searchStats.textContent = 'Введіть щонайменше 2 символи для пошуку...';
      searchResultsContainer.innerHTML = '';
      return;
    }

    // Filter segments
    let matchedSegments = bookData.segments.filter(seg => {
      if (activeSectionFilter !== 'all' && seg.section !== activeSectionFilter) {
        return false;
      }
      const titleLower = seg.title.toLowerCase();
      const textLower = seg.text.toLowerCase();
      const secLower = seg.section.toLowerCase();
      const idMatch = seg.id.toString() === q.replace(/^#/, '');

      return idMatch || terms.every(t => titleLower.includes(t) || textLower.includes(t) || secLower.includes(t));
    });

    searchStats.innerHTML = `Знайдено <strong>${matchedSegments.length}</strong> ${pluralizeSegments(matchedSegments.length)} за запитом «<em>${escapeHTML(q)}</em>»` + 
      (activeSectionFilter !== 'all' ? ` у розділі «${escapeHTML(activeSectionFilter)}»` : '');

    searchResultsContainer.innerHTML = '';

    if (matchedSegments.length === 0) {
      searchResultsContainer.innerHTML = `
        <div class="search-empty-state">
          <div style="font-size: 2.5rem; margin-bottom: 1rem;">🔍</div>
          <h3>Нічого не знайдено</h3>
          <p>Спробуйте змінити пошуковий запит або скинути фільтр за розділами.</p>
        </div>
      `;
      return;
    }

    matchedSegments.forEach(seg => {
      const card = document.createElement('div');
      card.className = 'bento-card search-result-card';

      const snippet = extractSnippet(seg.text, terms, 240);
      const highlightedSnippet = highlightTerms(escapeHTML(snippet), terms);
      const highlightedTitle = highlightTerms(escapeHTML(seg.title), terms);

      const pageLabel = seg.pages_label ? `с. ${seg.pages_label}` : `${seg.pages} стор.`;

      card.innerHTML = `
        <div class="search-card-header">
          <span class="search-card-sec">${escapeHTML(seg.section)}</span>
          <span class="seg-badge">#${seg.id}</span>
        </div>
        <h3 class="search-card-title">${highlightedTitle}</h3>
        <p class="search-card-snippet">${highlightedSnippet}</p>
        <div class="search-card-footer">
          <span class="seg-meta">${pageLabel} • ${formatWordCount(seg.text)}</span>
          <button class="btn-read-segment" data-id="${seg.id}">
            Читати повністю &rarr;
          </button>
        </div>
      `;

      card.addEventListener('click', () => {
        openReader(seg.id, terms);
      });

      searchResultsContainer.appendChild(card);
    });
  }

  // 4. Reader Modal Functionality
  function openReader(segmentId, highlightTermsList = null) {
    const seg = bookData.segments.find(s => s.id === segmentId);
    if (!seg) return;

    currentSegmentId = segmentId;
    window.location.hash = `segment-${segmentId}`;

    if (modalSectionTitle) modalSectionTitle.textContent = seg.section;
    if (modalSegmentTitle) modalSegmentTitle.textContent = seg.title;
    
    const pageLabel = seg.pages_label ? `Сторінки оригіналу: ${seg.pages_label}` : `${seg.pages} стор.`;
    if (modalSegmentMeta) {
      modalSegmentMeta.innerHTML = `
        <span>Сегмент <strong>#${seg.id}</strong> із ${bookData.segments.length}</span>
        <span>•</span>
        <span>${pageLabel}</span>
        <span>•</span>
        <span>${formatWordCount(seg.text)}</span>
      `;
    }

    // Format text: if subsegments exist and length > 1, render subsegments with page badges
    let bodyHTML = '';
    if (seg.subsegments && seg.subsegments.length > 1) {
      bodyHTML += `<div class="subsegments-accordion">`;
      bodyHTML += `<div style="margin-bottom: 1.5rem; color: var(--text-secondary); font-size: 0.95rem;">Сегмент містить <strong>${seg.subsegments.length}</strong> посторінкових підрозділів:</div>`;
      
      seg.subsegments.forEach(sub => {
        let subText = formatCleanTextToParagraphs(sub.text);
        if (highlightTermsList && highlightTermsList.length > 0) {
          subText = highlightTerms(subText, highlightTermsList);
        }
        bodyHTML += `
          <div class="subsegment-box" style="margin-bottom: 2rem; border-left: 3px solid var(--accent-primary); padding-left: 1.25rem;">
            <div class="subsegment-badge" style="display: inline-block; font-weight: 600; font-size: 0.82rem; color: var(--accent-primary); background: rgba(74, 144, 217, 0.1); padding: 0.2rem 0.65rem; border-radius: 6px; margin-bottom: 0.85rem;">
              📄 Частина ${sub.id} • ${escapeHTML(sub.pages || '')}
            </div>
            <div class="subsegment-content" style="line-height: 1.8; color: var(--text-primary); font-size: 1.05rem;">
              ${subText}
            </div>
          </div>
        `;
      });
      bodyHTML += `</div>`;
    } else {
      // Single continuous text
      let fullFormatted = formatCleanTextToParagraphs(seg.text);
      if (highlightTermsList && highlightTermsList.length > 0) {
        fullFormatted = highlightTerms(fullFormatted, highlightTermsList);
      }
      bodyHTML = `<div style="line-height: 1.8; color: var(--text-primary); font-size: 1.05rem;">${fullFormatted}</div>`;
    }

    modalSegmentBody.innerHTML = bodyHTML;

    // Prev / Next button states
    if (modalPrevBtn) modalPrevBtn.disabled = segmentId <= 1;
    if (modalNextBtn) modalNextBtn.disabled = segmentId >= bookData.segments.length;

    if (readerModal) {
      readerModal.classList.add('open');
      readerModal.classList.add('active');
      document.body.style.overflow = 'hidden';
      modalSegmentBody.scrollTop = 0;
    }
  }

  function closeReader() {
    if (readerModal) {
      readerModal.classList.remove('open');
      readerModal.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  // Navigation handlers
  if (modalPrevBtn) {
    modalPrevBtn.addEventListener('click', () => {
      if (currentSegmentId > 1) {
        openReader(currentSegmentId - 1);
      }
    });
  }

  if (modalNextBtn) {
    modalNextBtn.addEventListener('click', () => {
      if (currentSegmentId < bookData.segments.length) {
        openReader(currentSegmentId + 1);
      }
    });
  }

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', closeReader);
  }

  if (readerModal) {
    readerModal.addEventListener('click', (e) => {
      if (e.target === readerModal) {
        closeReader();
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (!readerModal || !readerModal.classList.contains('open')) return;
    if (e.key === 'Escape') {
      closeReader();
    } else if (e.key === 'ArrowLeft' && currentSegmentId > 1) {
      openReader(currentSegmentId - 1);
    } else if (e.key === 'ArrowRight' && currentSegmentId < bookData.segments.length) {
      openReader(currentSegmentId + 1);
    }
  });

  // Copy button
  if (modalCopyBtn) {
    modalCopyBtn.addEventListener('click', () => {
      const seg = bookData.segments.find(s => s.id === currentSegmentId);
      if (!seg) return;

      let textToCopy = `${seg.title}\nРозділ: ${seg.section}\nТ. Едвард Деймер — Атака на хибні міркування (7-е вид.)\nСторінки: ${seg.pages_label || seg.pages}\n\n${seg.text}`;

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(textToCopy).then(showCopyToast).catch(() => fallbackCopy(textToCopy));
      } else {
        fallbackCopy(textToCopy);
      }
    });
  }

  function fallbackCopy(text) {
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showCopyToast();
  }

  function showCopyToast() {
    if (!copyToast) return;
    copyToast.classList.add('show');
    setTimeout(() => {
      copyToast.classList.remove('show');
    }, 2500);
  }

  // Search input handlers
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      performSearch();
    });
  }

  if (searchClearBtn) {
    searchClearBtn.addEventListener('click', () => {
      if (searchInput) {
        searchInput.value = '';
        searchQuery = '';
        performSearch();
        searchInput.focus();
      }
    });
  }

  // Check URL hash on page load
  function checkHash() {
    const hash = window.location.hash;
    if (hash && hash.startsWith('#segment-')) {
      const id = parseInt(hash.replace('#segment-', ''), 10);
      if (!isNaN(id) && id >= 1 && id <= bookData.segments.length) {
        openReader(id);
      }
    }
  }

  // Helper Functions
  function escapeHTML(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function formatWordCount(text) {
    if (!text) return '0 слів';
    const words = text.trim().split(/\s+/).length;
    return `${words.toLocaleString('uk-UA')} слів`;
  }

  function pluralizeSegments(n) {
    const rem10 = n % 10;
    const rem100 = n % 100;
    if (rem100 >= 11 && rem100 <= 19) return 'сегментів';
    if (rem10 === 1) return 'сегмент';
    if (rem10 >= 2 && rem10 <= 4) return 'сегменти';
    return 'сегментів';
  }

  function formatCleanTextToParagraphs(text) {
    if (!text) return '';
    // Split sentences or groups of sentences into elegant readable paragraphs
    // A clean passage can be broken every 3-5 sentences or around key logical demarcations
    const raw = escapeHTML(text);
    
    // Check if there are natural boundaries like numbered items: "1. ", "2. ", "Принцип ", "Визначення."
    // Let's create paragraphs by splitting long texts around 400-600 characters at sentence endings.
    const sentences = raw.match(/[^.!?]+[.!?]+(?:["'»\)]|\s+|$)/g) || [raw];
    let paragraphs = [];
    let currentP = '';

    sentences.forEach(s => {
      if (currentP.length + s.length > 500 && currentP.length > 250) {
        paragraphs.push(`<p style="margin-bottom: 1.25rem;">${currentP.trim()}</p>`);
        currentP = s;
      } else {
        currentP += ' ' + s;
      }
    });

    if (currentP.trim().length > 0) {
      paragraphs.push(`<p style="margin-bottom: 1.25rem;">${currentP.trim()}</p>`);
    }

    return paragraphs.join('\n');
  }

  function extractSnippet(text, terms, maxLength = 240) {
    if (!text) return '';
    const lower = text.toLowerCase();
    
    let firstIndex = -1;
    for (const term of terms) {
      const idx = lower.indexOf(term);
      if (idx !== -1 && (firstIndex === -1 || idx < firstIndex)) {
        firstIndex = idx;
      }
    }

    if (firstIndex === -1) {
      return text.length <= maxLength ? text : text.substring(0, maxLength) + '…';
    }

    const start = Math.max(0, firstIndex - 60);
    const end = Math.min(text.length, firstIndex + maxLength - 60);
    let snippet = text.substring(start, end);
    if (start > 0) snippet = '…' + snippet;
    if (end < text.length) snippet += '…';
    return snippet;
  }

  function highlightTerms(htmlStr, terms) {
    if (!terms || terms.length === 0 || !htmlStr) return htmlStr;
    const sortedTerms = [...terms].sort((a, b) => b.length - a.length);
    const pattern = new RegExp(`(${sortedTerms.map(escapeRegex).join('|')})`, 'gi');
    return htmlStr.replace(pattern, '<mark class="search-highlight">$1</mark>');
  }

  function escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  // Initialize page
  initSectionFilters();
  renderTOC();
  searchStats.textContent = `Всього ${bookData.segments.length} сегментів книги (60 софізмів та логічних помилок)`;
  checkHash();
});
