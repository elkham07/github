from playwright.sync_api import Page, expect


def test_profile_page_loads(page: Page):
    page.goto('https://github.com/elkham07')
    expect(page).to_have_url('https://github.com/elkham07')


def test_open_repository_from_profile(page: Page):
    page.goto('https://github.com/elkham07')
    page.get_by_role('link', name='EM-Apex').click()
    expect(page).to_have_url('https://github.com/elkham07/EM-Apex')


def test_repositories_tab_visible(page: Page):
    page.goto('https://github.com/elkham07')
    expect(page.get_by_role('link', name='Repositories')).to_be_visible()


def test_followers_link_navigates(page: Page):
    page.goto('https://github.com/elkham07')
    page.get_by_role('link', name='followers').click()
    expect(page).to_have_url('https://github.com/elkham07?tab=followers')


def test_following_link_navigates(page: Page):
    page.goto('https://github.com/elkham07')
    page.get_by_role('link', name='following').click()
    expect(page).to_have_url('https://github.com/elkham07?tab=following')