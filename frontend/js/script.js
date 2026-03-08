// ── Company analysis ───────────────────────────────────────
async function analyzeCompany() {
  const urlInput = document.getElementById('urlInput');
  const url = urlInput.value.trim();

  if (!url) {
    shakeInput(urlInput);
    return;
  }

  const loading       = document.getElementById('loading');
  const resultSection = document.getElementById('resultSection');

  resultSection.classList.add('hidden');
  loading.classList.remove('hidden');

  try {
    const response = await fetch('/analyze-company', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url }),
    });

    if (!response.ok) throw new Error(`Server error: ${response.status}`);

    const data = await response.json();

    setField('company_name',      data.company_name);
    setField('industry',          data.industry);
    setField('summary',           data.summary);
    setField('products_services', data.products_services);
    setField('target_customers',  data.target_customers);
    setField('pain_points',       data.pain_points);

    loading.classList.add('hidden');
    resultSection.classList.remove('hidden');
    resultSection.scrollIntoView({ behavior: 'smooth', block: 'start' });

  } catch (error) {
    loading.classList.add('hidden');
    showError(error.message || 'Failed to analyze company. Please try again.');
  }
}

// ── Helpers ────────────────────────────────────────────────
function setField(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value || '—';
}

function shakeInput(inputEl) {
  inputEl.style.borderColor = 'rgba(248,113,113,0.6)';
  inputEl.style.boxShadow   = '0 0 0 3px rgba(248,113,113,0.15)';
  setTimeout(() => {
    inputEl.style.borderColor = '';
    inputEl.style.boxShadow   = '';
  }, 1200);
  inputEl.focus();
}

function showError(message) {
  const existing = document.getElementById('errorBanner');
  if (existing) existing.remove();

  const banner = document.createElement('div');
  banner.id = 'errorBanner';
  banner.style.cssText = `
    background:rgba(248,113,113,0.1);border:1px solid rgba(248,113,113,0.3);
    border-radius:10px;padding:14px 18px;font-size:14px;color:#fca5a5;
    margin-bottom:20px;display:flex;align-items:center;gap:10px;
    animation:fadeIn 0.2s ease;
  `;
  banner.innerHTML = `
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/>
      <line x1="12" y1="16" x2="12.01" y2="16"/>
    </svg>${message}`;

  const inputCard = document.querySelector('.input-card');
  if (inputCard) inputCard.insertAdjacentElement('afterend', banner);
  setTimeout(() => banner.remove(), 5000);
}

// ── Enter key ──────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('urlInput');
  if (input) input.addEventListener('keydown', e => { if (e.key === 'Enter') analyzeCompany(); });
});