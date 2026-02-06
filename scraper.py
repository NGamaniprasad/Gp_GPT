from playwright.sync_api import sync_playwright
import re

def scrape_comments(url):
    results = []

    try:
        with sync_playwright() as p:
            print("Launching browser...")
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.set_default_timeout(15000)

            print("Opening URL...")
            page.goto(url, wait_until="domcontentloaded")

            for _ in range(3):
                page.mouse.wheel(0, 2000)
                page.wait_for_timeout(1000)

            print("Extracting text...")
            text = page.inner_text("body")

            emails = re.findall(
                r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
                text
            )

            for email in set(emails):
                results.append(["Unknown", email, "Unknown"])

            browser.close()
            print("Done.")

    except Exception as e:
        print("SCRAPER ERROR:", e)

    return results
