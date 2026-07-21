from playwright.sync_api import Page

def test_search(page: Page):
    page.goto('https://github.com/')
    page.get_by_role('button', name='Search').click()
    page.get_by_role('combobox', name='Search').click()
    page.get_by_role('combobox', name='Search').fill('react')
    page.get_by_role('combobox', name='Search').press('Enter')


def test2_search(page: Page):
    page.goto('https://github.com/')
    page.get_by_role('button', name='Search').click()
    page.get_by_role('combobox', name='Search').press('Enter')


def test3_search(page: Page):
    page.goto('https://github.com/')
    page.get_by_role('button', name='Search').click()
    page.get_by_role('combobox', name='Search').click()
    page.get_by_role('combobox', name='Search').fill('qwezxc123456fghjk')
    page.get_by_role('combobox', name='Search').press('Enter')


