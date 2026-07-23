from pages.base_page import BasePage


class RepoPage(BasePage):
    def __init__(self, page, owner: str, repo: str):
        super().__init__(page)
        self.owner = owner
        self.repo = repo
        self.url = f"https://github.com/{owner}/{repo}"

    def open_repo(self):
        self.open(self.url)

    def open_issues_tab(self):
        self.page.get_by_role('link', name='Issues', exact=True).click()

    def filter_closed_issues(self):
        self.open(f"{self.url}/issues")
        self.page.get_by_role('link', name='Closed  (0)').click()

    def open_pull_requests_tab(self):
        self.page.get_by_role('link', name='Pull requests', exact=True).click()

    def open_actions_tab(self):
        self.page.get_by_role('link', name='Actions').click()

    def open_code_tab(self):
        self.page.get_by_role('link', name='Code').click()

    def open_folder(self, folder_name: str):
        self.page.get_by_role('link', name=folder_name).click()

    def open_file(self, file_name: str):
        self.page.get_by_role('link', name=file_name).click()