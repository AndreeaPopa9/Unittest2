from pages.dropdown_page import Dropdown_page

class Dropdown(Dropdown_page):
    dropdown = Dropdown_page()

    def test_select_first_option(self):
        self.dropdown.select_first_option()

    def test_select_second_option(self):
        self.dropdown.select_second_option()

