/**
 * AlignAI Prompt Hub — Analytics + Copy + Collapse
 */
(function() {
  'use strict';

  function track(event, props) {
    if (typeof console !== 'undefined') {
      console.debug('[AlignAI Analytics]', event, props || {});
    }
  }

  track('page_view', {
    path: window.location.pathname,
    referrer: document.referrer,
  });

  // Copy prompt to clipboard
  document.addEventListener('click', function(e) {
    var btn = e.target.closest('.btn-copy-prompt');
    if (!btn) return;
    var promptId = btn.dataset.promptId;
    var model = btn.dataset.model;
    var panel = document.getElementById('panel-' + model);
    if (!panel) return;
    var fullEl = panel.querySelector('.prompt-text-full code');
    if (!fullEl) {
      var previewEl = panel.querySelector('.prompt-text-preview code');
      if (previewEl) fullEl = previewEl;
    }
    if (!fullEl) return;
    var text = fullEl.textContent;
    navigator.clipboard.writeText(text).then(function() {
    var orig = btn.textContent;
      btn.textContent = 'Copied!';
      btn.style.opacity = '0.7';
      setTimeout(function() {
        btn.textContent = orig;
        btn.style.opacity = '1';
      }, 2000);
    });
    track('prompt_copy', { prompt_id: promptId, model: model });
  });

  // Collapse/expand full prompt
  document.addEventListener('click', function(e) {
    var btn = e.target.closest('.btn-toggle-prompt');
    if (!btn) return;
    var target = btn.closest('.gated-content') || btn.parentElement;
    var pre = target.querySelector('.prompt-text-full');
    if (!pre) return;
    var isCollapsed = pre.classList.toggle('prompt-collapsed');
    btn.textContent = isCollapsed ? 'Show Full Prompt' : 'Collapse Prompt';
  });

  window.AlignAIAnalytics = { track: track };
})();
