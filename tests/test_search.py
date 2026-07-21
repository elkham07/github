from playwright.sync_api import Page

def test_search(page: Page):
    page.goto('https://github.com/')
    