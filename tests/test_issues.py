from playwright.sync_api import Page, expect

from playwright.sync_api import Page, expect


def test_open_repository(page: Page):
    page.goto('https://github.com/elkham07')
    page.get_by_role('link', name='EM-Apex').click()
    expect(page).to_have_url('https://github.com/elkham07/EM-Apex')


def test_open_issues_tab(page: Page):
    page.goto('https://github.com/elkham07/EM-Apex')
    page.get_by_role('link', name='Issues', exact=True).click()
    expect(page).to_have_url('https://github.com/elkham07/EM-Apex/issues')



def test_closed_issues_filter(page: Page):
    page.goto('https://github.com/elkham07/EM-Apex/issues')
    page.get_by_role('link', name='Closed  (0)').click()
    expect(page).to_have_url('https://github.com/elkham07/EM-Apex/issues?q=is%3Aissue%20state%3Aclosed')


def test_open_pull_requests_tab(page: Page):
    page.goto('https://github.com/elkham07/EM-Apex')
    page.get_by_role('link', name='Pull requests', exact=True).click()
    expect(page).to_have_url('https://github.com/elkham07/EM-Apex/pulls')


def test_open_actions_tab(page: Page):
    page.goto('https://github.com/elkham07/EM-Apex')
    page.get_by_role('link', name='Actions').click()
    expect(page).to_have_url('https://github.com/elkham07/EM-Apex/actions')


def test_open_code_tab(page: Page):
    page.goto('https://github.com/elkham07/EM-Apex')
    page.get_by_role('link', name='Code').click()
    expect(page).to_have_url('https://github.com/elkham07/EM-Apex')


def test_open_folder_in_code(page: Page):
    page.goto('https://github.com/elkham07/EM-Apex')
    page.get_by_role('link', name='Refine UI Elements, (').click()
    expect(page).to_have_url("https://github.com/elkham07/EM-Apex/tree/main/Refine%20UI%20Elements")


def test_open_file_in_code(page: Page):
    page.goto('https://github.com/elkham07/EM-Apex')
    page.get_by_role('link', name='Refine UI Elements, (').click()
    page.get_by_role('link', name='vite.config.ts, (File)').click()
    expect(page).to_have_url("https://github.com/elkham07/EM-Apex/blob/main/Refine%20UI%20Elements/vite.config.ts")