#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
import time

def take_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 800})

        html_path = '/Users/justinalex/Desktop/Apex One Website/index.html'
        screenshots_dir = '/Users/justinalex/Desktop/Apex One Website/screenshots'

        # 1. Homepage hero
        page.goto(f'file://{html_path}')
        time.sleep(1)
        page.screenshot(path=f'{screenshots_dir}/01-homepage-hero.png')
        print("✓ 01-homepage-hero.png")

        # 2. Trust bar
        page.evaluate('window.scrollBy(0, 400)')
        time.sleep(0.5)
        page.screenshot(path=f'{screenshots_dir}/02-trust-bar.png')
        print("✓ 02-trust-bar.png")

        # 3. Owner portal hero
        page.goto(f'file://{html_path}')
        time.sleep(1)
        page.click('button:text("I\'m an Owner")')
        time.sleep(1)
        page.screenshot(path=f'{screenshots_dir}/03-owner-hero.png')
        print("✓ 03-owner-hero.png")

        # 4. Owner services
        page.evaluate('window.scrollBy(0, 600)')
        time.sleep(0.5)
        page.screenshot(path=f'{screenshots_dir}/04-owner-services.png')
        print("✓ 04-owner-services.png")

        # 5. Owner benefits
        page.evaluate('window.scrollBy(0, 800)')
        time.sleep(0.5)
        page.screenshot(path=f'{screenshots_dir}/05-owner-benefits.png')
        print("✓ 05-owner-benefits.png")

        # 6. Tenant portal hero
        page.goto(f'file://{html_path}')
        time.sleep(1)
        page.click('button:text("I\'m a Tenant")')
        time.sleep(1)
        page.screenshot(path=f'{screenshots_dir}/06-tenant-hero.png')
        print("✓ 06-tenant-hero.png")

        # 7. Tenant why rent
        page.evaluate('window.scrollBy(0, 600)')
        time.sleep(0.5)
        page.screenshot(path=f'{screenshots_dir}/07-tenant-why-rent.png')
        print("✓ 07-tenant-why-rent.png")

        # 8. Tenant process
        page.evaluate('window.scrollBy(0, 600)')
        time.sleep(0.5)
        page.screenshot(path=f'{screenshots_dir}/08-tenant-process.png')
        print("✓ 08-tenant-process.png")

        # 9. Tenant testimonials
        page.evaluate('window.scrollBy(0, 600)')
        time.sleep(0.5)
        page.screenshot(path=f'{screenshots_dir}/09-tenant-testimonials.png')
        print("✓ 09-tenant-testimonials.png")

        # 10. Footer
        page.evaluate('window.scrollBy(0, 1200)')
        time.sleep(0.5)
        page.screenshot(path=f'{screenshots_dir}/10-footer.png')
        print("✓ 10-footer.png")

        # 11. Rentals page hero + filter
        rentals_path = '/Users/justinalex/Desktop/Apex One Website/rentals.html'
        page.goto(f'file://{rentals_path}')
        time.sleep(1)
        page.screenshot(path=f'{screenshots_dir}/11-rentals-hero-filter.png')
        print("✓ 11-rentals-hero-filter.png")

        # 12. Rentals listings grid
        page.evaluate('window.scrollBy(0, 400)')
        time.sleep(0.5)
        page.screenshot(path=f'{screenshots_dir}/12-rentals-grid.png')
        print("✓ 12-rentals-grid.png")

        # 13. Rentals CTA + footer
        page.evaluate('window.scrollBy(0, 1000)')
        time.sleep(0.5)
        page.screenshot(path=f'{screenshots_dir}/13-rentals-cta.png')
        print("✓ 13-rentals-cta.png")

        browser.close()
        print("\n✅ All screenshots captured!")

if __name__ == '__main__':
    take_screenshots()
