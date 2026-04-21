/**
 * AlignAI Prompt Hub — homepage search
 *
 * Fetches /search-index.json (built by build.py) and filters prompts
 * client-side as the user types. Matches against title, use_case (subtitle),
 * tags, category name, and difficulty.
 *
 * Renders results into #search-results. No-op if the search input isn't on
 * the page (so it's safe to load globally).
 */
(function () {
  'use strict';

  const input = document.getElementById('prompt-search');
  const resultsEl = document.getElementById('search-results');
  if (!input || !resultsEl) return;

  let index = [];
  let loaded = false;
  let loading = false;
  let debounceTimer = null;

  // Load the search index lazily on first focus or first keypress.
  function loadIndex() {
    if (loaded || loading) return Promise.resolve();
    loading = true;
    return fetch('/search-index.json', { cache: 'force-cache' })
      .then(function (r) {
        if (!r.ok) throw new Error('Search index unavailable');
        return r.json();
      })
      .then(function (data) {
        index = Array.isArray(data) ? data : (data.prompts || []);
        loaded = true;
        loading = false;
      })
      .catch(function (err) {
        loading = false;
        console.error('[search] failed to load index:', err);
      });
  }

  function escapeHtml(str) {
    return String(str || '').replace(/[&<>"']/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c];
    });
  }

  function highlight(text, terms) {
    let out = escapeHtml(text);
    terms.forEach(function (t) {
      if (!t) return;
      const re = new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
      out = out.replace(re, '<mark>$1</mark>');
    });
    return out;
  }

  function score(item, terms) {
    // Sum: title hit = 5, tag exact = 4, category = 3, use_case hit = 2, difficulty = 1.
    let s = 0;
    const title = (item.title || '').toLowerCase();
    const useCase = (item.use_case || '').toLowerCase();
    const cat = (item.category_name || item.category_slug || '').toLowerCase();
    const diff = (item.difficulty || '').toLowerCase();
    const tags = (item.tags || []).map(function (t) { return String(t).toLowerCase(); });

    terms.forEach(function (t) {
      if (!t) return;
      if (title.indexOf(t) !== -1) s += 5;
      if (tags.indexOf(t) !== -1) s += 4;
      else if (tags.some(function (tag) { return tag.indexOf(t) !== -1; })) s += 2;
      if (cat.indexOf(t) !== -1) s += 3;
      if (useCase.indexOf(t) !== -1) s += 2;
      if (diff.indexOf(t) !== -1) s += 1;
    });
    return s;
  }

  function render(query) {
    const q = (query || '').trim().toLowerCase();
    if (!q) {
      resultsEl.innerHTML = '';
      resultsEl.style.display = 'none';
      return;
    }
    if (!loaded) {
      resultsEl.innerHTML = '<p class="search-status">Loading prompt index…</p>';
      resultsEl.style.display = 'block';
      return;
    }

    const terms = q.split(/\s+/).filter(Boolean);
    const matches = index
      .map(function (item) { return { item: item, s: score(item, terms) }; })
      .filter(function (x) { return x.s > 0; })
      .sort(function (a, b) { return b.s - a.s; })
      .slice(0, 12);

    if (matches.length === 0) {
      resultsEl.innerHTML = '<p class="search-status">No prompts matched <strong>' + escapeHtml(q) + '</strong>. Try a category or task keyword.</p>';
      resultsEl.style.display = 'block';
      return;
    }

    const html = '<ul class="search-result-list" role="listbox">' +
      matches.map(function (m) {
        const it = m.item;
        const url = '/prompts/' + encodeURIComponent(it.slug) + '/';
        const catLabel = it.category_name || it.category_slug || '';
        return '<li class="search-result-item" role="option">' +
          '<a href="' + url + '" class="search-result-link">' +
          '<span class="search-result-cat">' + escapeHtml(catLabel) + '</span>' +
          '<span class="search-result-title">' + highlight(it.title || '', terms) + '</span>' +
          (it.use_case ? '<span class="search-result-snippet">' + highlight(it.use_case, terms) + '</span>' : '') +
          '</a>' +
          '</li>';
      }).join('') +
      '</ul>';
    resultsEl.innerHTML = html;
    resultsEl.style.display = 'block';
  }

  function onInput() {
    const q = input.value;
    if (debounceTimer) clearTimeout(debounceTimer);
    debounceTimer = setTimeout(function () {
      if (!loaded) {
        loadIndex().then(function () { render(q); });
      } else {
        render(q);
      }
    }, 80);
  }

  input.addEventListener('focus', loadIndex, { once: true });
  input.addEventListener('input', onInput);

  // Clear results on Escape
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      input.value = '';
      render('');
    }
  });
})();
