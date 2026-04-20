# Apex One Property Management — Claude Instructions

You're working on **Apex One**, a dual-path property management website for Metro Detroit. The site has two completely separate user experiences: **Owner Portal** and **Tenant Portal**.

## Architecture Overview

### Dual-Path Design
The site uses a **selection-based architecture** where users choose their role on the homepage:
1. **Homepage** → User selects "I'm an Owner" or "I'm a Tenant"
2. **Owner Portal** → Property management services (tenant screening, maintenance, rent collection)
3. **Tenant Portal** → Housing search and rental application

Both experiences are built in a **single HTML file** (`index.html`) with JavaScript handling visibility toggling. Users can switch between portals using "Switch to [Other] Portal" buttons in each nav.

## Design System

### Colors
```
--navy:        #0A1628   (Primary dark background)
--gold:        #D4A017   (Primary accent/CTA)
--royal:       #1A4FBB   (Secondary accent, section labels)
--white:       #FFFFFF   (Card backgrounds)
--body:        #111111   (Primary text)
--muted:       #666      (Secondary text)
--light-bg:    #F9F8F6   (Light background)
--badge-bg:    #F0F4FF   (Badge backgrounds)
```

### Typography
**Fonts:**
- **Headlines**: Plus Jakarta Sans (700 weight, -0.02em letter-spacing)
- **Body text**: Inter (400 weight, 1.6 line-height)
- **Nav links**: Inter (500 weight, uppercase, 0.08em letter-spacing, 13px)

**Hierarchy:**
- H1 (Hero): 56px–80px, Plus Jakarta Sans 800
- H2 (Section): 40px–48px, Plus Jakarta Sans 800
- H3 (Card): 18px, Plus Jakarta Sans 700
- Body: 14px–15px, Inter 400
- Small/label: 12px–13px, Inter 500–600, uppercase

### Components

**Cards:**
- Background: white (#FFFFFF)
- Border-radius: 20px
- Box-shadow: 0 4px 24px rgba(0,0,0,0.08)
- Border: 1px solid rgba(0,0,0,0.06)
- Padding: 32px
- Hover: translateY(-4px), shadow: 0 12px 40px rgba(0,0,0,0.12)

**Buttons:**
- Border-radius: 100px (fully rounded pill shape)
- Padding: 14px 28px
- Font: Plus Jakarta Sans, 600 weight
- Gold variant: gold background, dark text
- Outline variant: transparent, dark border
- Hover: smooth transitions, subtle lift

**Nav buttons (Pill buttons):**
- Border-radius: 100px
- Padding: 10px 20px
- Font: Inter, 500 weight, uppercase, 0.08em letter-spacing
- Size: 13px

**Badges/Labels** (like "Property Owner" on testimonials):
- Background: #F0F4FF
- Color: #1A4FBB
- Border-radius: 100px
- Padding: 4px 14px
- Font-size: 12px
- Font-weight: 600

**Section Labels** (above headings):
- Font-size: 12px
- Font-weight: 600
- Letter-spacing: 0.1em
- Text-transform: uppercase
- Color: var(--royal)
- Margin-bottom: 12px

### Spacing
- **Between sections**: 100px top/bottom padding
- **Container max-width**: 1100px
- **Container padding**: 48px (desktop), 24px (mobile)
- **Card gap**: 24–28px
- **Section gap**: 100px (vertical)

## File Structure

```
/Apex One Website/
├── index.html              # Single-file SPA (Owner + Tenant portals)
├── CLAUDE.md              # This file
├── screenshots/           # Section screenshots for review
│   ├── 01-homepage-selection.png
│   ├── 02-owner-hero.png
│   ├── 03-owner-services.png
│   ├── 04-owner-benefits.png
│   ├── 05-owner-cta.png
│   ├── 06-tenant-hero.png
│   ├── 07-tenant-why-rent.png
│   ├── 08-tenant-process.png
│   ├── 09-tenant-testimonials.png
│   └── 10-footer.png
```

## How to Operate

### Starting the Dev Server
```bash
cd "/Users/justinalex/Desktop/Apex One Website"
python3 -m http.server 3001
# Open http://localhost:3001
```

### Making Changes
1. **Edit `index.html`** for all changes (HTML, CSS, JS)
2. **Test both portals**: Click "I'm an Owner" and "I'm a Tenant" to verify both paths work
3. **Use the switch buttons**: Verify owners can switch to tenant view and vice versa
4. **Screenshot sections**: After visual changes, take fresh screenshots for verification

### Typography Updates
- Always import both Plus Jakarta Sans AND Inter from Google Fonts
- Headlines: `font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 700; letter-spacing: -0.02em;`
- Body: `font-family: 'Inter', sans-serif; font-weight: 400; line-height: 1.6;`

### Component Updates
When modifying cards, buttons, or sections:
1. Maintain the 100px top/bottom padding on section dividers
2. Keep card border-radius at 20px (not 14px or 16px)
3. Use the proper box-shadow: `0 4px 24px rgba(0,0,0,0.08)`
4. Always include borders: `1px solid rgba(0,0,0,0.06)`
5. Test hover states on all interactive elements

## Visual Verification

After any CSS or layout changes:
1. Take a screenshot of the affected section
2. Compare to previous screenshots
3. Verify both desktop and mobile (if responsive changes)
4. Check both Owner and Tenant portals if the change affects both

**Screenshot process:**
```bash
# Screenshots are stored in /screenshots/
# Use Python + Playwright to capture:
python3 << 'EOF'
from playwright.sync_api import sync_playwright
# ... (script to capture the affected section)
EOF
```

## Known Constraints

- **Single HTML file**: All code (HTML, CSS, JS) lives in one `index.html`
- **No build process**: No webpack, no bundling — direct browser execution
- **Vanilla JavaScript**: No frameworks, just native DOM manipulation for portal switching
- **CSS-only animations**: Keep animations lightweight and CSS-based

## Navigation & Switching

**Homepage:**
- Two large CTA buttons: "I'm an Owner" and "I'm a Tenant"

**Owner Portal Nav:**
- Logo, links (About, Services, Contact)
- **"Switch to Tenant Portal"** button
- Filled gold "Owner Portal" button

**Tenant Portal Nav:**
- Logo, links (Available Units, About, Contact)
- **"Switch to Owner Portal"** button
- Filled gold "Tenant Portal" button

Users can click the switch buttons anytime to toggle between portals (scrolls to top automatically).

## Content Specifications

### Owner Portal Sections
1. **Hero Card** — Property image (left), content (right), stats, CTA
2. **Services** — 3 cards: Tenant Screening, Maintenance Coordination, Rent Collection
3. **Why Choose Us** — Heading + 4 bullet points with gold checkmarks
4. **CTA Banner** — "Ready to Maximize Your Rental Income?" with free analysis button
5. **Footer** — Multi-column with links, contact info, social icons

### Tenant Portal Sections
1. **Hero** — Headline, subheading, two CTAs (Browse Units, Schedule Tour)
2. **Why Rent From Us** — 3 benefit cards (Professional Management, Well-Maintained, Fair Pricing)
3. **Get Housed in 3 Steps** — Process steps with numbered circles and connector line
4. **What Tenants Say** — 3 testimonial cards with stars, quote, author, and role badge
5. **CTA Banner** — "Ready to Find Your Next Home?" with search button
6. **Footer** — Same multi-column layout as owner

## The Self-Improvement Loop

When you update the site:
1. **Make the change** in `index.html`
2. **Take screenshots** to verify the result
3. **Compare to previous screenshots** to ensure quality
4. **Update this file** if you discover constraints, style rules, or naming conventions
5. **Document what you learned** for the next instance

## Bottom Line

This is a **corporate, professional dual-path website** built for two distinct audiences. Maintain consistency across both portals while respecting the separate user journeys. Keep the design clean, the typography precise, and the interactions smooth.

Estately-inspired aesthetic: pills, cards, generous spacing, strong typography hierarchy, and polished interactions.

Stay consistent. Stay professional. Keep improving.
