/**
 * Олена Щербина - Логічний аналіз юридичної аргументації (Київ, 2014)
 * Інтерактивний рідер та повнотекстовий пошук
 * Vanilla JS
 */

document.addEventListener('DOMContentLoaded', () => {
  const bookData = window.SCHERBINA_DATA;
  if (!bookData || !bookData.segments) {
    console.error('Дані книги Олени Щербини не завантажено.');
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
      
      // Short label for filter chips
      let shortLabel = sec;
      if (sec.includes('.')) {
        shortLabel = sec.split('.')[0] + (sec.includes(':') ? ':' : '') + ' ' + sec.split('.')[1].trim().substring(0, 32) + '…';
      }
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

        const pageLabel = seg.page_str ? `с. ${seg.page_str}` : `${seg.pages} стор.`;
        const subBadge = seg.subsegments && seg.subsegments.length > 1
          ? ` • ${seg.subsegments.length} підрозділів`
          : '';

        item.innerHTML = `
          <div class="toc-item-left">
            <span class="seg-number">#${seg.id}</span>
            <div class="seg-info">
              <span class="seg-title">${escapeHTML(seg.title)}</span>
              <span class="seg-meta">${pageLabel} • ${formatCharCount(seg.text.length)}${subBadge}</span>
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
      searchStats.textContent = `Всього ${bookData.segments.length} сегментів дисертації (424 сторінки)`;
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

      const pageLabel = seg.page_str ? `с. ${seg.page_str}` : `${seg.pages} стор.`;

      card.innerHTML = `
        <div class="search-card-header">
          <span class="search-card-sec">${escapeHTML(seg.section)}</span>
          <span class="seg-badge">#${seg.id}</span>
        </div>
        <h3 class="search-card-title">${highlightedTitle}</h3>
        <p class="search-card-snippet">${highlightedSnippet}</p>
        <div class="search-card-footer">
          <span class="seg-meta">${pageLabel} • ${formatCharCount(seg.text.length)}</span>
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
    
    const pageLabel = seg.page_str ? `Сторінки оригіналу: ${seg.page_str}` : `${seg.pages} стор.`;
    if (modalSegmentMeta) {
      modalSegmentMeta.innerHTML = `
        <span>Сегмент <strong>#${seg.id}</strong> із ${bookData.segments.length}</span>
        <span>•</span>
        <span>${pageLabel}</span>
        <span>•</span>
        <span>${formatCharCount(seg.text.length)}</span>
      `;
    }

    // Format text paragraphs
    let bodyHTML = formatSegmentMarkdown(seg.text);
    if (highlightTermsList && highlightTermsList.length > 0) {
      bodyHTML = highlightTerms(bodyHTML, highlightTermsList);
    }
    modalSegmentBody.innerHTML = bodyHTML;

    // Subsegments breakdown if more than 1
    if (seg.subsegments && seg.subsegments.length > 1) {
      const subContainer = document.createElement('div');
      subContainer.className = 'subsegments-accordion';
      subContainer.innerHTML = `<h4 style="margin: 2rem 0 1rem; font-size: 1.15rem; color: var(--accent-primary); border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem;">📄 Посторінковий поділ (${seg.subsegments.length} сторінок/частин):</h4>`;
      
      seg.subsegments.forEach(sub => {
        const subItem = document.createElement('div');
        subItem.className = 'subsegment-box';
        let subText = formatSegmentMarkdown(sub.text);
        if (highlightTermsList && highlightTermsList.length > 0) {
          subText = highlightTerms(subText, highlightTermsList);
        }
        subItem.innerHTML = `
          <div class="subsegment-badge">Частина ${sub.id} • ${escapeHTML(sub.pages || '')}</div>
          <div class="subsegment-content">${subText}</div>
        `;
        subContainer.appendChild(subItem);
      });
      modalSegmentBody.appendChild(subContainer);
    }

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
    if (e.key === 'Escape' && readerModal && readerModal.classList.contains('open')) {
      closeReader();
    }
  });

  // Copy button
  if (modalCopyBtn) {
    modalCopyBtn.addEventListener('click', () => {
      const seg = bookData.segments.find(s => s.id === currentSegmentId);
      if (!seg) return;

      let textToCopy = `${seg.title}\n(${seg.section})\nОлена Щербина — Логічний аналіз юридичної аргументації (Київ, 2014)\n\n${seg.text}`;

      navigator.clipboard.writeText(textToCopy).then(() => {
        showCopyToast();
      }).catch(() => {
        const ta = document.createElement('textarea');
        ta.value = textToCopy;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        showCopyToast();
      });
    });
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

  // Markdown & Text Formatter
  function escapeHTML(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function formatCharCount(chars) {
    return Math.round(chars / 6) + ' слів';
  }

  function formatSegmentMarkdown(rawText) {
    if (!rawText) return '';

    // Split lines
    const lines = rawText.split('\n');
    let outHtml = '';
    let inList = false;
    let listType = 'ul';

    const closeListIfNeeded = () => {
      if (inList) {
        outHtml += listType === 'ol' ? '</ol>\n' : '</ul>\n';
        inList = false;
      }
    };

    for (let i = 0; i < lines.length; i++) {
      let line = lines[i].trim();

      if (!line) {
        closeListIfNeeded();
        continue;
      }

      // Page comment: <!-- Page 123 -->
      const pageMatch = line.match(/^<!--\s*Page\s+(\d+)\s*-->/i);
      if (pageMatch) {
        closeListIfNeeded();
        outHtml += `<div class="doc-page-marker"><span class="doc-page-badge">📄 Сторінка ${pageMatch[1]}</span></div>\n`;
        continue;
      }

      // Horizontal rule: ---
      if (/^---+$/.test(line)) {
        closeListIfNeeded();
        outHtml += '<hr class="doc-divider">\n';
        continue;
      }

      // Headings: #, ##, ###, ####
      if (line.startsWith('#### ')) {
        closeListIfNeeded();
        outHtml += `<h5 class="doc-h5">${formatInline(line.substring(5))}</h5>\n`;
        continue;
      }
      if (line.startsWith('### ')) {
        closeListIfNeeded();
        outHtml += `<h4 class="doc-h4">${formatInline(line.substring(4))}</h4>\n`;
        continue;
      }
      if (line.startsWith('## ')) {
        closeListIfNeeded();
        outHtml += `<h3 class="doc-h3">${formatInline(line.substring(3))}</h3>\n`;
        continue;
      }
      if (line.startsWith('# ')) {
        closeListIfNeeded();
        outHtml += `<h2 class="doc-h2">${formatInline(line.substring(2))}</h2>\n`;
        continue;
      }

      // Blockquote: > ...
      if (line.startsWith('>')) {
        closeListIfNeeded();
        const quoteContent = line.replace(/^>\s?/, '');
        outHtml += `<blockquote class="doc-quote">${formatInline(quoteContent)}</blockquote>\n`;
        continue;
      }

      // Bullet list item: - or *
      const bulletMatch = line.match(/^[-*]\s+(.*)/);
      if (bulletMatch) {
        if (!inList || listType !== 'ul') {
          closeListIfNeeded();
          outHtml += '<ul class="doc-list">\n';
          inList = true;
          listType = 'ul';
        }
        outHtml += `<li>${formatInline(bulletMatch[1])}</li>\n`;
        continue;
      }

      // Numbered list item: 1. or 2)
      const numMatch = line.match(/^\d+[\.\)]\s+(.*)/);
      if (numMatch) {
        if (!inList || listType !== 'ol') {
          closeListIfNeeded();
          outHtml += '<ol class="doc-list doc-ol">\n';
          inList = true;
          listType = 'ol';
        }
        outHtml += `<li>${formatInline(numMatch[1])}</li>\n`;
        continue;
      }

      // Normal paragraph
      closeListIfNeeded();
      outHtml += `<p class="doc-p">${formatInline(line)}</p>\n`;
    }

    closeListIfNeeded();
    return outHtml;
  }

  function formatInline(str) {
    if (!str) return '';
    let out = escapeHTML(str);
    // Bold: **text**
    out = out.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    // Italic: *text*
    out = out.replace(/\*(.*?)\*/g, '<em>$1</em>');
    // Inline code: `code`
    out = out.replace(/`([^`]+)`/g, '<code>$1</code>');
    return out;
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
