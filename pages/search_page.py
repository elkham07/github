from pages.base_page import BasePage

class SearchPage(BasePage):
    URL = "https://github.com/"

    def open_search(self):
        self.open(self.URL)
        self.page.get_by_role('button', name='Search').click()

        def search_for(self, query: str):
            self.page.get_by_role('combobox', name='Search').click()
            self.page.get_by_role('combobox',name='Search').fill(query)
            self.page.get_by_role('combobox', name='Search').press('Enter')

        def search_empty(self):
         self.page.get_by_role('combobox', name='Search').press('Enter')  


        def filter_by_language(self, language: str):
            self.page.get_by_role('link', name=language).press('Enter')  
