/**
 * AlignAI Prompt Hub — Email Gate (Simple Capture)
 * Collects email, stores in Supabase, unlocks content immediately.
 * No magic link, no authentication — just email capture.
 */
(function() {
  'use strict';

  var SUPABASE_URL = 'https://ojrswncqntvyoorgdyen.supabase.co';
  var SUPABASE_KEY = 'sb_publishable_sNPKZFuhATv5eJka-RUCag_QKnCwE6M';
  var STORAGE_KEY = 'alignai_prompt_email';
  var supabase = null;

  function initSupabase() {
    try {
      if (window.supabase && window.supabase.createClient) {
        supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
      }
    } catch (e) {}
  }

  function getSavedEmail() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      return null;
    }
  }

  function saveEmail(email) {
    try {
      localStorage.setItem(STORAGE_KEY, email);
    } catch (e) {}
  }

  function revealGatedContent() {
    document.querySelectorAll('.gated-overlay').forEach(function(el) {
      el.style.display = 'none';
    });
    document.querySelectorAll('.gated-content').forEach(function(el) {
      el.classList.add('gated-unlocked');
    });
  }

  function showMessage(container, msg, isError) {
    var msgEl = container.querySelector('.gate-message');
    if (!msgEl) {
      msgEl = document.createElement('p');
      msgEl.className = 'gate-message';
      msgEl.style.fontSize = '13px';
      msgEl.style.marginTop = '0.5rem';
      container.appendChild(msgEl);
    }
    msgEl.textContent = msg;
    msgEl.style.color = isError ? '#EF5350' : '#00C853';
  }

  function handleUnlock(btn) {
    var container = btn.closest('.gated-overlay-cta');
    var emailInput = container.querySelector('.gate-email-input');
    var email = emailInput ? emailInput.value.trim() : '';

    if (!email || email.indexOf('@') < 0 || email.indexOf('.') < 0) {
      showMessage(container, 'Please enter a valid email address.', true);
      return;
    }

    btn.disabled = true;
    btn.textContent = 'Unlocking...';

    // Store email locally
    saveEmail(email);

    // Store in Supabase (fire and forget)
    if (supabase) {
      supabase.from('prompt_hub_signups').insert({
        email: email,
        source: 'prompt_gate',
        page_url: window.location.pathname
      }).then(function() {}).catch(function() {});
    }

    // Unlock immediately
    revealGatedContent();
  }

  function bindUnlockButtons() {
    document.querySelectorAll('.btn-gate-unlock').forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        handleUnlock(btn);
      });
    });

    document.querySelectorAll('.gate-email-input').forEach(function(input) {
      input.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          var btn = input.closest('.gated-overlay-cta').querySelector('.btn-gate-unlock');
          if (btn) handleUnlock(btn);
        }
      });
    });
  }

  function init() {
    initSupabase();

    // Already unlocked?
    if (getSavedEmail()) {
      revealGatedContent();
      return;
    }

    // Bind unlock buttons
    bindUnlockButtons();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.AlignAIAuth = {
    isAuthenticated: function() { return !!getSavedEmail(); },
    revealGatedContent: revealGatedContent,
  };
})();
