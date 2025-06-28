from playwright.sync_api import sync_playwright
import time

def scrape_and_screenshot(url, screenshot_path="screenshot.png"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        page.screenshot(path=screenshot_path)

        content = page.locator("body").inner_text()
        browser.close()
        return content

url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
chapter_text = scrape_and_screenshot(url)
with open("chapter1.txt", "w", encoding="utf-8") as f:
    f.write(chapter_text)
print("Scraped and saved.")