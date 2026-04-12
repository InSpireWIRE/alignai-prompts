/**
 * AlignAI Prompt Hub — Auth Gate
 * Controls visibility of gated-content elements.
 * Gated content (full prompt text) is hidden by default via CSS.
 * This script reveals it after authentication.
 */

(function() {
  'use strict';

  const AUTH_KEY = 'alignai_auth_token';

  function isAuthenticated() {
    // Check for auth token (set by sign-in flow)
    try {
      return !!sessionStorage.getItem(AUTH_KEY);
    } catch (e) {
      return false;
    }
  }

  function revealGatedContent() {
    document.querySelectorAll('.gated-content').forEach(el => {
      el.classList.add('gated-unlocked');
    });
  }

  function showSignInPrompt() {
    // Intercept copy buttons for unauthenticated users
    document.querySelectorAll('.btn-copy-prompt').forEach(btn => {
      btn.addEventListener('click', function(e) {
        if (!isAuthenticated()) {
          e.preventDefault();
          e.stopImmediatePropagation();
          // Trigger sign-in modal
          const signinBtn = document.getElementById('btn-signin');
          if (signinBtn) signinBtn.click();
        }
      }, true);
    });
  }

  function init() {
    if (isAuthenticated()) {
      revealGatedContent();
    } else {
      showSignInPrompt();
    }
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose for external use
  window.AlignAIAuth = {
    isAuthenticated: isAuthenticated,
    revealGatedContent: revealGatedContent,
  };
})();
