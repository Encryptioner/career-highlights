/**
 * Career Highlights — Google Analytics event tracking module.
 *
 * Vanilla JS (no build step). JSDoc types provide editor safety without TypeScript.
 * All events are anonymous — no PII is ever sent.
 */

// ── Type definitions ──────────────────────────────────────────────────────────

/**
 * @typedef {
 *   | { name: 'viz_viewed',           params: { title: string, domain: string, category: string } }
 *   | { name: 'viz_navigated',        params: { direction: 'next' | 'prev', from_index: number } }
 *   | { name: 'viz_downloaded',       params: { title: string, domain: string } }
 *   | { name: 'viz_zoomed',           params: { method: 'button' | 'scroll' | 'pinch' | 'double_tap', zoom_level: number } }
 *   | { name: 'viz_panned' }
 *   | { name: 'domain_filtered',      params: { domain: 'all' | 'personal_career' | 'nerddevs_professional' | 'personal_projects' | 'nerddevs_projects' } }
 *   | { name: 'category_filtered',    params: { category: 'all' | 'featured' | 'timeline_growth' | 'technology_mastery' | 'business_impact' | 'project_portfolio' } }
 *   | { name: 'external_link_clicked', params: { label: string, destination: 'portfolio' | 'linkedin' | 'github' | 'blog' } }
 *   | { name: 'section_scrolled',     params: { section: 'hero' | 'gallery' | 'footer' } }
 *   | { name: 'error_occurred',       params: { category: string, action: string, error: string } }
 * } AnalyticsEvent
 */

// ── Core tracking function ────────────────────────────────────────────────────

/**
 * Send a typed analytics event to Google Analytics.
 * No-ops gracefully when gtag is unavailable (ad blockers, offline).
 *
 * @param {AnalyticsEvent} event
 * @returns {void}
 */
function trackEvent(event) {
  if (typeof window === 'undefined' || typeof window.gtag !== 'function') return;

  const { name, ...rest } = event;
  const params = 'params' in rest ? rest.params : undefined;
  window.gtag('event', name, params);
}

// ── Helpers ───────────────────────────────────────────────────────────────────

const _EMAIL_PATTERN = /[\w.+-]+@[\w.-]+\.\w+/g;

/**
 * Strip email addresses from error messages and truncate to 100 chars.
 * Prevents accidental PII leakage in error_occurred events.
 *
 * @param {string} msg
 * @returns {string}
 */
function sanitizeError(msg) {
  return String(msg).replace(_EMAIL_PATTERN, '[email]').slice(0, 100);
}

/**
 * Map internal config domain keys to GA-friendly domain values.
 *
 * @param {string} configDomain - Domain key from career-highlights-config.json
 * @returns {'all' | 'personal_career' | 'nerddevs_professional' | 'personal_projects' | 'nerddevs_projects'}
 */
function mapDomainKey(configDomain) {
  const MAP = {
    'all':                  'all',
    'personal':             'personal_career',
    'professional':         'nerddevs_professional',
    'personal-projects':    'personal_projects',
    'professional-projects':'nerddevs_projects',
  };
  return MAP[configDomain] || 'all';
}

/**
 * Map internal config category keys to GA-friendly category values.
 *
 * @param {string} configCategory - Category key from career-highlights-config.json
 * @returns {'all' | 'featured' | 'timeline_growth' | 'technology_mastery' | 'business_impact' | 'project_portfolio'}
 */
function mapCategoryKey(configCategory) {
  const MAP = {
    'all':        'all',
    'featured':   'featured',
    'timeline':   'timeline_growth',
    'technology': 'technology_mastery',
    'business':   'business_impact',
    'projects':   'project_portfolio',
  };
  return MAP[configCategory] || 'all';
}

// ── Export ────────────────────────────────────────────────────────────────────

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { trackEvent, sanitizeError, mapDomainKey, mapCategoryKey };
}
