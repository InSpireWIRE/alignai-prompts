/**
 * AlignAI Prompt Hub — Analytics
 * Lightweight event tracking. Replace with Cloudflare Web Analytics
 * or Plausible in production.
 */

(function() {
  'use strict';

  function track(event, props) {
    if (typeof console !== 'undefined') {
      console.debug('[AlignAI Analytics]', event, props || {});
    }
    // Placeholder: send to analytics endpoint
    // fetch('/api/track', { method: 'POST', body: JSON.stringify({ event, ...props }) });
  }

  // Track page view
  track('page_view', {
    path: window.location.pathname,
    referrer: document.referrer,
  });

  // Track prompt copy events
  document.addEventListener('click', function(e) {
    const btn = e.target.closest('.btn-copy-prompt');
    if (btn) {
      track('prompt_copy', {
        prompt_id: btn.dataset.promptId,
        model: btn.dataset.model,
      });
    }
  });

  window.AlignAIAnalytics = { track: track };
})();
