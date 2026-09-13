/**
 * Логіка (підручник НЮУ ім. Ярослава Мудрого) - Interactive Reader & Search
 * Pure Vanilla JS
 */

document.addEventListener('DOMContentLoaded', () => {
  const bookData = window.LOGICA_TEXTBOOK_DATA;
  if (!bookData || !bookData.segments) {
    console.error('Book data not loaded.');
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
    allBtn.textContent = `Усі розділи (${bookData.segments.length})`;
    allBtn.addEventListener('click', () => setSectionFilter('all'));
    sectionFilterContainer.appendChild(allBtn);

    bookData.sections.forEach(sec => {
      const count = bookData.segments.filter(s => s.section === sec).length;
      const btn = document.createElement('button');
      btn.className = 'filter-chip';
      btn.dataset.section = sec;
      
      // Shorten label for chip if long
      let label = sec;
      if (label.startsWith('Розділ ')) {
        const parts = label.split('.');
        label = parts[0] + (parts[1] ? '.' + parts[1] : '');
      }
      btn.textContent = `${label} (${count})`;
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

  // 2. Render Table of Contents (Grouped by Sections)
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
        item.innerHTML = `
          <div class="toc-item-left">
            <span class="seg-number">#${seg.id}</span>
            <div class="seg-info">
              <span class="seg-title">${escapeHTML(seg.title)}</span>
              <span class="seg-meta">${seg.pages > 1 ? seg.pages + ' стор.' : '1 стор.'} • ${formatWordCount(seg.text.length)}</span>
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

  // 3. Fast Live Search Across Segments
  function performSearch() {
    const q = searchQuery.trim().toLowerCase();
    
    if (q === '') {
      tocViewSection.style.display = 'block';
      searchViewSection.style.display = 'none';
      if (searchClearBtn) searchClearBtn.style.display = 'none';
      searchStats.textContent = `Всього ${bookData.segments.length} сегментів підручника`;
      return;
    }

    if (searchClearBtn) searchClearBtn.style.display = 'block';
    tocViewSection.style.display = 'none';
    searchViewSection.style.display = 'block';

    const rawTerms = q.split(/\s+/).filter(t => t.length > 0);

    const filtered = bookData.segments.filter(seg => {
      // Check section filter
      if (activeSectionFilter !== 'all' && seg.section !== activeSectionFilter) {
        return false;
      }
      
      const titleLower = seg.title.toLowerCase();
      const textLower = seg.text.toLowerCase();
      const secLower = seg.section.toLowerCase();

      return rawTerms.every(term => 
        titleLower.includes(term) || textLower.includes(term) || secLower.includes(term)
      );
    });

    searchStats.innerHTML = `Знайдено <strong>${filtered.length}</strong> ${pluralizeSegments(filtered.length)} за запитом «${escapeHTML(q)}»`;

    renderSearchResults(filtered, rawTerms);
  }

  function renderSearchResults(results, terms) {
    if (!searchResultsContainer) return;
    searchResultsContainer.innerHTML = '';

    if (results.length === 0) {
      searchResultsContainer.innerHTML = `
        <div class="empty-search-state bento-card">
          <div style="font-size: 2.5rem; margin-bottom: 1rem;">🔍</div>
          <h3>Нічого не знайдено</h3>
          <p style="color: var(--text-secondary); margin-bottom: 1.5rem;">
            Спробуйте перевірити правопис, скористатися синонімами або вибрати фільтр «Усі розділи».
          </p>
          <button class="btn btn-secondary" id="reset-search-btn">Очистити пошук</button>
        </div>
      `;
      const resetBtn = document.getElementById('reset-search-btn');
      if (resetBtn) {
        resetBtn.addEventListener('click', () => {
          searchInput.value = '';
          searchQuery = '';
          performSearch();
        });
      }
      return;
    }

    results.forEach(seg => {
      const card = document.createElement('div');
      card.className = 'bento-card search-result-card';
      
      const snippet = extractSnippet(seg.text, terms, 240);
      const highlightedTitle = highlightTerms(seg.title, terms);
      const highlightedSnippet = highlightTerms(snippet, terms);

      card.innerHTML = `
        <div class="search-card-header">
          <span class="search-card-section">${escapeHTML(seg.section)}</span>
          <span class="seg-badge">#${seg.id}</span>
        </div>
        <h3 class="search-card-title">${highlightedTitle}</h3>
        <p class="search-card-snippet">${highlightedSnippet}</p>
        <div class="search-card-footer">
          <span class="seg-meta">${seg.pages} стор. • ${formatWordCount(seg.text.length)}</span>
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

    modalSectionTitle.textContent = seg.section;
    modalSegmentTitle.textContent = seg.title;
    modalSegmentMeta.innerHTML = `
      <span>Сегмент <strong>#${seg.id}</strong> із ${bookData.segments.length}</span>
      <span>•</span>
      <span>${seg.pages > 1 ? seg.pages + ' сторінок' : '1 сторінка'}</span>
      <span>•</span>
      <span>${formatWordCount(seg.text.length)}</span>
    `;

    // Render formatted text or subsegments
    if (seg.subsegments && seg.subsegments.length > 0) {
      let bodyHTML = '';
      seg.subsegments.forEach((sub, idx) => {
        let subText = formatSegmentText(sub.text);
        if (highlightTermsList && highlightTermsList.length > 0) {
          subText = highlightTerms(subText, highlightTermsList);
        }
        const pagesLabel = sub.pages ? `Сторінки ${escapeHTML(sub.pages)}` : '';
        bodyHTML += `
          <div class="subsegment-box" style="margin-bottom: 1.5rem;">
            ${pagesLabel ? `<div class="subsegment-badge">Підсегмент ${sub.id || (idx + 1)} • ${pagesLabel}</div>` : ''}
            <div class="subsegment-content" style="font-size: 1.05rem; line-height: 1.8; color: var(--text-primary);">${subText}</div>
          </div>
        `;
      });
      modalSegmentBody.innerHTML = bodyHTML;
    } else {
      let bodyHTML = formatSegmentText(seg.text);
      if (highlightTermsList && highlightTermsList.length > 0) {
        bodyHTML = highlightTerms(bodyHTML, highlightTermsList);
      }
      modalSegmentBody.innerHTML = bodyHTML;
    }

    // Prev / Next button states
    modalPrevBtn.disabled = segmentId <= 1;
    modalNextBtn.disabled = segmentId >= bookData.segments.length;

    readerModal.classList.add('open');
    document.body.style.overflow = 'hidden';
    modalSegmentBody.scrollTop = 0;
  }

  function closeReader() {
    readerModal.classList.remove('open');
    document.body.style.overflow = '';
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

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (!readerModal.classList.contains('open')) return;
    if (e.key === 'Escape') {
      closeReader();
    } else if (e.key === 'ArrowLeft' && currentSegmentId > 1) {
      openReader(currentSegmentId - 1);
    } else if (e.key === 'ArrowRight' && currentSegmentId < bookData.segments.length) {
      openReader(currentSegmentId + 1);
    }
  });

  // Copy segment text
  if (modalCopyBtn) {
    modalCopyBtn.addEventListener('click', () => {
      const seg = bookData.segments.find(s => s.id === currentSegmentId);
      if (!seg) return;

      const citation = `\n\n— Логіка: підручник / За заг. ред. О. Г. Данильяна (НЮУ ім. Ярослава Мудрого). Харків: Право, 2022 (#${seg.id}: ${seg.title})`;
      const textToCopy = seg.text + citation;

      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast('Текст сегменту скопійовано з посиланням!');
      }).catch(() => {
        showToast('Не вдалося скопіювати текст.');
      });
    });
  }

  function showToast(msg) {
    if (!copyToast) return;
    copyToast.textContent = msg;
    copyToast.classList.add('show');
    setTimeout(() => {
      copyToast.classList.remove('show');
    }, 2800);
  }

  // Input search events
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      performSearch();
    });
  }

  if (searchClearBtn) {
    searchClearBtn.addEventListener('click', () => {
      searchInput.value = '';
      searchQuery = '';
      searchInput.focus();
      performSearch();
    });
  }

  // Check URL Hash on Load (e.g. #segment-9)
  function checkHash() {
    const hash = window.location.hash;
    if (hash && hash.startsWith('#segment-')) {
      const id = parseInt(hash.replace('#segment-', ''), 10);
      if (!isNaN(id) && id >= 1 && id <= bookData.segments.length) {
        openReader(id);
      }
    }
  }

  // Helpers
  function escapeHTML(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function formatWordCount(chars) {
    return Math.round(chars / 6) + ' слів';
  }

  function formatSegmentText(rawText) {
    if (!rawText) return '';
    const cleaned = escapeHTML(rawText);
    const paragraphs = cleaned.split(/\n\s*\n|\n/).filter(p => p.trim() !== '');
    if (paragraphs.length <= 1) {
      const sentences = cleaned.match(/[^.!?]+[.!?]+["']?|[^.!?]+$/g) || [cleaned];
      let res = '';
      let cur = '';
      sentences.forEach((s, idx) => {
        cur += s + ' ';
        if ((idx + 1) % 3 === 0 || idx === sentences.length - 1) {
          res += `<p>${cur.trim()}</p>`;
          cur = '';
        }
      });
      return res || `<p>${cleaned}</p>`;
    }
    return paragraphs.map(p => `<p>${p}</p>`).join('');
  }

  function extractSnippet(text, terms, maxLength) {
    if (!text) return '';
    const lower = text.toLowerCase();
    let firstIndex = -1;

    for (const t of terms) {
      const idx = lower.indexOf(t);
      if (idx !== -1 && (firstIndex === -1 || idx < firstIndex)) {
        firstIndex = idx;
      }
    }

    if (firstIndex === -1) {
      return text.substring(0, maxLength) + (text.length > maxLength ? '…' : '');
    }

    const start = Math.max(0, firstIndex - 60);
    const end = Math.min(text.length, firstIndex + maxLength - 60);
    let snippet = text.substring(start, end);

    if (start > 0) snippet = '… ' + snippet;
    if (end < text.length) snippet = snippet + ' …';

    return snippet;
  }

  function highlightTerms(text, terms) {
    if (!text || !terms || terms.length === 0) return text;
    let result = text;
    const sortedTerms = [...terms].sort((a, b) => b.length - a.length);
    sortedTerms.forEach(term => {
      if (!term || term.length < 2) return;
      const regex = new RegExp(`(${escapeRegex(term)})`, 'gi');
      result = result.replace(regex, '<mark class="search-highlight">$1</mark>');
    });
    return result;
  }

  function escapeRegex(str) {
    return str.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
  }

  function pluralizeSegments(count) {
    const mod10 = count % 10;
    const mod100 = count % 100;
    if (mod100 >= 11 && mod100 <= 19) return 'сегментів';
    if (mod10 === 1) return 'сегмент';
    if (mod10 >= 2 && mod10 <= 4) return 'сегменти';
    return 'сегментів';
  }

  // Initialize
  initSectionFilters();
  renderTOC();
  checkHash();
});
