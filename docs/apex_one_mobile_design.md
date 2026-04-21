# Apex One Property Management — Mobile Design Guide
## Maximizing Professional Look & Feel on Mobile

---

## Core Philosophy
Apex One serves two distinct mobile audiences: property owners checking their income and performance on the go, and tenants looking for homes, paying rent, and submitting maintenance requests. Both expect a professional, trustworthy experience similar to a financial services app or real estate portal. Mobile must feel polished, fast, and easy to navigate with one thumb.

---

## Design System Reference
```css
:root {
  /* Colors */
  --navy: #0A1628;
  --gold: #D4A017;
  --blue: #1A4FBB;
  --off-white: #F8F8F8;
  --text-dark: #111111;
  --text-grey: #666666;
  --text-light: #A0AEC0;
  --white: #FFFFFF;
  --gold-dark: #B8860B;
  
  /* Shadows */
  --shadow-sm: 0 2px 8px rgba(0,0,0,0.06);
  --shadow-md: 0 4px 24px rgba(0,0,0,0.08);
  --shadow-lg: 0 8px 40px rgba(0,0,0,0.12);
  
  /* Border radius */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-pill: 100px;
}
```

---

## Breakpoints
```css
/* Mobile first */
/* Base: 0px+ */
/* Tablet: 768px+ */
/* Desktop: 1024px+ */

@media (min-width: 768px) { /* tablet */ }
@media (min-width: 1024px) { /* desktop */ }
@media (min-width: 1280px) { /* wide */ }
```

---

## Typography Scale (Mobile)
```css
:root {
  /* Mobile sizes */
  --text-xs: 11px;
  --text-sm: 13px;
  --text-base: 15px;
  --text-lg: 17px;
  --text-xl: 20px;
  --text-2xl: 24px;
  --text-3xl: 28px;
  --text-4xl: 34px;
  --text-hero: 38px;
}

/* Scale up on desktop */
@media (min-width: 1024px) {
  :root {
    --text-hero: 56px;
    --text-4xl: 48px;
    --text-3xl: 36px;
  }
}

/* Section label (e.g. "FOR OWNERS") */
.section-label {
  font-size: var(--text-xs);
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 12px;
}
```

---

## Spacing (Mobile)
```css
:root {
  --section-padding-mobile: 56px 20px;
  --section-padding-tablet: 80px 40px;
  --section-padding-desktop: 100px 80px;
  --card-padding-mobile: 20px;
  --card-padding-desktop: 32px;
  --container-max: 1200px;
}

.container {
  width: 100%;
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 20px;
}

@media (min-width: 1024px) {
  .container {
    padding: 0 40px;
  }
}
```

---

## Nav — Mobile Behavior
```css
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  height: 64px;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--navy);
  transition: height 0.3s ease, box-shadow 0.3s ease;
}

/* Shrink on scroll */
.nav.scrolled {
  height: 52px;
  box-shadow: 0 2px 20px rgba(0,0,0,0.3);
  backdrop-filter: blur(10px);
}

/* Hide desktop links on mobile */
.nav-center {
  display: none;
}

@media (min-width: 1024px) {
  .nav-center {
    display: flex;
    gap: 8px;
  }
}

/* Hamburger */
.hamburger {
  display: flex;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 10px;
  margin-right: -10px;
}

.hamburger span {
  width: 22px;
  height: 2px;
  background: white;
  border-radius: 2px;
  transition: all 0.3s ease;
  display: block;
}

.hamburger.open span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}
.hamburger.open span:nth-child(2) {
  opacity: 0;
  transform: scaleX(0);
}
.hamburger.open span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

@media (min-width: 1024px) {
  .hamburger { display: none; }
}

/* Mobile drawer */
.mobile-drawer {
  position: fixed;
  top: 64px;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--navy);
  z-index: 999;
  padding: 32px 24px;
  display: flex;
  flex-direction: column;
  transform: translateX(100%);
  transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  overflow-y: auto;
}

.mobile-drawer.open {
  transform: translateX(0);
}

.mobile-drawer a {
  color: white;
  font-size: 20px;
  font-weight: 700;
  padding: 16px 0;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  text-decoration: none;
  display: block;
}

.mobile-drawer a.active {
  color: var(--gold);
}

/* Portal buttons in drawer */
.mobile-drawer .portal-buttons {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 32px;
}

.mobile-drawer .btn {
  width: 100%;
  text-align: center;
  padding: 14px;
}
```

---

## Cards — Mobile Grid
```css
/* Default: single column on mobile */
.cards-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

/* 2 columns at tablet */
@media (min-width: 640px) {
  .cards-grid { grid-template-columns: repeat(2, 1fr); }
}

/* 3 columns at desktop */
@media (min-width: 1024px) {
  .cards-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
  }
}

/* Card base */
.card {
  background: white;
  border-radius: var(--radius-lg);
  padding: var(--card-padding-mobile);
  border: 1px solid rgba(0,0,0,0.06);
  box-shadow: var(--shadow-md);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

@media (min-width: 1024px) {
  .card {
    padding: var(--card-padding-desktop);
  }
  .card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
  }
}
```

---

## Buttons — Touch Optimized
```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 48px; /* Meets WCAG touch target */
  padding: 12px 24px;
  border-radius: var(--radius-pill);
  font-family: inherit;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
  -webkit-tap-highlight-color: transparent;
  border: none;
  text-decoration: none;
}

/* Gold filled */
.btn-gold {
  background: var(--gold);
  color: var(--text-dark);
}
.btn-gold:hover { background: var(--gold-dark); }
.btn-gold:active { transform: scale(0.97); }

/* Navy filled */
.btn-navy {
  background: var(--navy);
  color: white;
}

/* White outlined */
.btn-outline-white {
  background: transparent;
  color: white;
  border: 1.5px solid rgba(255,255,255,0.5);
}
.btn-outline-white:hover {
  background: rgba(255,255,255,0.1);
}

/* Navy outlined */
.btn-outline-navy {
  background: transparent;
  color: var(--navy);
  border: 1.5px solid var(--navy);
}

/* Full width on mobile */
@media (max-width: 639px) {
  .btn-full-mobile { width: 100%; }
}

/* Button group */
.btn-group {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

@media (max-width: 479px) {
  .btn-group {
    flex-direction: column;
  }
  .btn-group .btn {
    width: 100%;
  }
}
```

---

## Rental Listing Cards — Mobile
```css
.listing-card {
  background: white;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(0,0,0,0.06);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

@media (min-width: 1024px) {
  .listing-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
  }
}

/* Image area */
.listing-image {
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #0A1628, #112240);
  position: relative;
  overflow: hidden;
}

/* Neighborhood badge */
.listing-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  background: var(--blue);
  color: white;
  font-size: 11px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: var(--radius-pill);
  letter-spacing: 0.02em;
}

/* Card body */
.listing-body {
  padding: 16px;
}

.listing-price {
  font-size: 24px;
  font-weight: 800;
  color: var(--gold);
  letter-spacing: -0.02em;
  margin-bottom: 4px;
}

.listing-address {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 10px;
}

/* Bed/Bath/Sqft row */
.listing-details {
  display: flex;
  gap: 12px;
  font-size: 12px;
  color: var(--text-grey);
  margin-bottom: 10px;
  flex-wrap: wrap;
}

/* Card buttons */
.listing-actions {
  display: flex;
  gap: 8px;
  margin-top: 14px;
}

.listing-actions .btn {
  flex: 1;
  min-height: 44px;
  font-size: 13px;
  padding: 10px 16px;
}
```

---

## Filter Bar — Mobile
```css
.filter-bar {
  background: white;
  padding: 16px 20px;
  border-bottom: 1px solid rgba(0,0,0,0.06);
  position: sticky;
  top: 64px;
  z-index: 50;
  box-shadow: var(--shadow-sm);
}

/* Stack filters vertically on mobile */
.filter-controls {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

@media (min-width: 768px) {
  .filter-controls {
    flex-direction: row;
    align-items: center;
    flex-wrap: wrap;
  }
}

/* Bedroom toggle pills */
.bedroom-filters {
  display: flex;
  gap: 8px;
}

.bedroom-btn {
  min-width: 44px;
  min-height: 44px;
  border-radius: var(--radius-pill);
  border: 1.5px solid rgba(0,0,0,0.15);
  background: white;
  font-weight: 600;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
  -webkit-tap-highlight-color: transparent;
}

.bedroom-btn.active {
  background: var(--gold);
  border-color: var(--gold);
  color: var(--text-dark);
}

/* Select dropdowns */
.filter-select {
  height: 44px;
  border-radius: var(--radius-pill);
  border: 1.5px solid rgba(0,0,0,0.15);
  padding: 0 16px;
  font-size: 14px; /* Must be 16px on iOS to prevent zoom */
  font-size: max(14px, 16px);
  font-family: inherit;
  background: white;
  cursor: pointer;
  width: 100%;
}

@media (min-width: 768px) {
  .filter-select {
    width: auto;
    min-width: 160px;
  }
}
```

---

## Accordion (FAQ) — Mobile
```css
.accordion-item {
  background: white;
  border-radius: var(--radius-lg);
  margin-bottom: 8px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  border: 1px solid rgba(0,0,0,0.06);
}

.accordion-header {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 20px;
  background: none;
  border: none;
  text-align: left;
  cursor: pointer;
  font-family: inherit;
  font-size: 15px;
  font-weight: 600;
  color: var(--text-dark);
  gap: 12px;
  min-height: 56px; /* Generous touch target */
  -webkit-tap-highlight-color: transparent;
}

.accordion-chevron {
  width: 20px;
  height: 20px;
  color: var(--gold);
  flex-shrink: 0;
  transition: transform 0.3s ease;
}

.accordion-item.open .accordion-chevron {
  transform: rotate(180deg);
}

.accordion-body {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.35s ease, padding 0.35s ease;
  padding: 0 20px;
}

.accordion-item.open .accordion-body {
  max-height: 500px;
  padding: 0 20px 20px;
}

.accordion-body p {
  font-size: 14px;
  line-height: 1.7;
  color: var(--text-grey);
}
```

---

## Scroll Animations
```javascript
// Intersection Observer for scroll animations
const animateOnScroll = () => {
  const elements = document.querySelectorAll('.animate');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const delay = entry.target.dataset.delay || 0;
        setTimeout(() => {
          entry.target.classList.add('animated');
        }, parseInt(delay));
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -40px 0px'
  });
  
  elements.forEach((el, i) => {
    // Auto-stagger grid children
    const parent = el.parentElement;
    if (parent.classList.contains('cards-grid') || 
        parent.classList.contains('cards-row')) {
      const siblings = Array.from(parent.children);
      el.dataset.delay = siblings.indexOf(el) * 80;
    }
    observer.observe(el);
  });
};

/* CSS */
.animate {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.animate.animated {
  opacity: 1;
  transform: translateY(0);
}

/* Slide in from left */
.animate-left {
  opacity: 0;
  transform: translateX(-20px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.animate-left.animated {
  opacity: 1;
  transform: translateX(0);
}

/* Respect reduced motion */
@media (prefers-reduced-motion: reduce) {
  .animate, .animate-left {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

---

## Nav Shrink on Scroll
```javascript
const nav = document.querySelector('.nav');
let lastScroll = 0;

window.addEventListener('scroll', () => {
  const currentScroll = window.scrollY;
  
  // Shrink after 40px
  if (currentScroll > 40) {
    nav.classList.add('scrolled');
  } else {
    nav.classList.remove('scrolled');
  }
  
  lastScroll = currentScroll;
}, { passive: true }); // passive for better mobile performance
```

---

## Page Transitions
```javascript
// Fade in on load
document.addEventListener('DOMContentLoaded', () => {
  document.body.style.opacity = '0';
  document.body.style.transition = 'opacity 0.4s ease';
  
  requestAnimationFrame(() => {
    document.body.style.opacity = '1';
  });
});

// Fade out on navigate
document.querySelectorAll('a[href]').forEach(link => {
  // Only internal links, not anchors or external
  const href = link.getAttribute('href');
  if (href && !href.startsWith('#') && !href.startsWith('http') && 
      !href.startsWith('mailto') && !href.startsWith('tel')) {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      document.body.style.opacity = '0';
      setTimeout(() => {
        window.location.href = href;
      }, 200);
    });
  }
});
```

---

## Trust Bar — Mobile
```css
/* Stack trust items on mobile */
.trust-bar {
  background: white;
  padding: 32px 20px;
  border-top: 1px solid rgba(0,0,0,0.06);
  border-bottom: 1px solid rgba(0,0,0,0.06);
}

.trust-bar-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  text-align: center;
}

@media (min-width: 768px) {
  .trust-bar-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

.trust-stat-number {
  font-size: 36px;
  font-weight: 800;
  color: var(--blue);
  letter-spacing: -0.02em;
  line-height: 1;
  margin-bottom: 4px;
}

.trust-stat-label {
  font-size: 12px;
  color: var(--text-grey);
  font-weight: 500;
}
```

---

## Forms — Mobile Optimized
```css
.form-group {
  margin-bottom: 16px;
}

.form-label {
  display: block;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-dark);
  margin-bottom: 8px;
}

.form-input,
.form-select,
.form-textarea {
  width: 100%;
  height: 52px;
  padding: 0 16px;
  border-radius: var(--radius-md);
  border: 1.5px solid rgba(0,0,0,0.12);
  font-family: inherit;
  font-size: 16px; /* Prevent iOS zoom */
  color: var(--text-dark);
  background: white;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
  -webkit-appearance: none;
  appearance: none;
}

.form-textarea {
  height: auto;
  min-height: 120px;
  padding: 14px 16px;
  resize: vertical;
}

.form-input:focus,
.form-select:focus,
.form-textarea:focus {
  outline: none;
  border-color: var(--gold);
  box-shadow: 0 0 0 3px rgba(212, 160, 23, 0.1);
}

/* Error state */
.form-input.error {
  border-color: #e53e3e;
  box-shadow: 0 0 0 3px rgba(229, 62, 62, 0.1);
}

.form-error-msg {
  font-size: 12px;
  color: #e53e3e;
  margin-top: 4px;
}
```

---

## Footer — Mobile
```css
.footer {
  background: var(--navy);
  padding: 48px 20px 32px;
}

/* Stack columns on mobile */
.footer-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 32px;
  margin-bottom: 40px;
}

@media (min-width: 768px) {
  .footer-grid {
    grid-template-columns: 2fr 1fr 1fr 1fr;
    gap: 40px;
  }
}

.footer-col-title {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text-light);
  margin-bottom: 16px;
}

.footer-link {
  display: block;
  color: rgba(255,255,255,0.6);
  font-size: 14px;
  text-decoration: none;
  padding: 5px 0;
  transition: color 0.2s;
}

.footer-link:hover {
  color: white;
}

/* Social icons */
.footer-socials {
  display: flex;
  gap: 12px;
  margin-top: 20px;
}

.social-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255,255,255,0.6);
  transition: all 0.2s;
  -webkit-tap-highlight-color: transparent;
}

.social-icon:hover {
  border-color: var(--gold);
  color: var(--gold);
}

/* Bottom bar */
.footer-bottom {
  padding-top: 24px;
  border-top: 1px solid rgba(255,255,255,0.08);
  display: flex;
  flex-direction: column;
  gap: 12px;
  font-size: 12px;
  color: rgba(255,255,255,0.4);
}

@media (min-width: 768px) {
  .footer-bottom {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
}
```

---

## iOS/Android Fixes
```css
/* Safe area for notched phones */
.nav {
  padding-top: env(safe-area-inset-top);
}

.mobile-drawer {
  padding-bottom: env(safe-area-inset-bottom);
}

.footer {
  padding-bottom: max(32px, env(safe-area-inset-bottom));
}

/* Fix 100vh on iOS */
.hero, .full-screen {
  min-height: 100svh;
}

/* Prevent text size adjust on rotation */
html {
  -webkit-text-size-adjust: 100%;
}

/* Remove tap highlight globally */
* {
  -webkit-tap-highlight-color: transparent;
}

/* Prevent double-tap zoom on buttons */
button, a {
  touch-action: manipulation;
}

/* Fix input zoom on iOS */
input, select, textarea {
  font-size: 16px !important;
}
```

---

## Performance Checklist
```
□ All images have width + height attributes set
□ Images use loading="lazy" except above-fold
□ Animations use only transform and opacity (GPU accelerated)
□ scroll event listeners use { passive: true }
□ No layout thrashing (batch DOM reads/writes)
□ Fonts preloaded in <head>
□ CSS animations paused when tab not visible
```

---

## Pre-Launch Mobile Testing Checklist
- [ ] iPhone SE (375px) — smallest common screen
- [ ] iPhone 14 (390px)
- [ ] Samsung Galaxy (360px)
- [ ] iPad (768px)
- [ ] All buttons have minimum 44px touch target
- [ ] No horizontal scroll on any page
- [ ] Forms don't zoom on focus (iOS)
- [ ] Hamburger menu works smoothly
- [ ] Accordion FAQ works with touch
- [ ] Filter bar works on mobile
- [ ] Page transitions smooth
- [ ] Safe area insets working on notched phones
- [ ] Footer not cut off by home indicator

---

*Apex One Mobile Design Guide v1.0*
*For use with Claude Code — drop into project folder*
