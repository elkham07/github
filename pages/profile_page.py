from pages.base_page import BasePage 


class ProfilePage(BasePage):
    URL= "https://github.com/elkham07"

    def open_profile(self):
        self.open(self.URL)


    def open_repository(self, repo_name: str):
        self.page.get_by_role('link', name=repo_name).click()

    
    def open_followers(self):
        self.page.get_by_role('link', name='followers').click()

    
    def open_following(self):
        self.page.get_by_role('link', name='following').click()


    def get_nickname_locator(self):
        return self.page.locator('.p-nickname')
    
