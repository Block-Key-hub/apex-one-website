#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
import time

def capture_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 800})

        # Load the HTML file directly
        html_path = '/Users/justinalex/Desktop/Apex One Website/index.html'
        page.goto(f'file://{html_path}')
        time.sleep(2)

        # Screenshot 1: Homepage with hero and trust bar
        page.screenshot(path='screenshots/01-homepage-hero-trustbar.png')
        print("✓ Screenshot 1: Homepage Hero with Trust Bar")

        # Screenshot 2: Owner Portal Hero with updated image
        page.click('button:text("I\'m an Owner")')
        time.sleep(1)
        page.screenshot(path='screenshots/02-owner-hero-card.png')
        print("✓ Screenshot 2: Owner Hero Card (navy gradient + grid pattern + gold accent)")

        # Screenshot 3: Service Cards (improved shadows)
        page.evaluate('window.scrollBy(0, 600)')
        time.sleep(0.5)
        page.screenshot(path='screenshots/03-owner-services.png')
        print("✓ Screenshot 3: Service Cards (improved depth)")

        # Screenshot 4: CTA Section (updated button styling)
        page.evaluate('window.scrollBy(0, 1000)')
        time.sleep(0.5)
        page.screenshot(path='screenshots/04-owner-cta.png')
        print("✓ Screenshot 4: CTA Section (updated button styling)")

        # Screenshot 5: Tenant Portal
        page.goto(f'file://{html_path}')
        time.sleep(1)
        page.click('button:text("I\'m a Tenant")')
        time.sleep(1)
        page.screenshot(path='screenshots/05-tenant-hero.png')
        print("✓ Screenshot 5: Tenant Hero")

        browser.close()
        print("\n✅ All screenshots captured successfully!")

if __name__ == '__main__':
    capture_screenshots()
