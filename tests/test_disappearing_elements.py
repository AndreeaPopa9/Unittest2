from pages.disappearing_elements_page import Disappearing_elements_page

class Disappearing_elements(Disappearing_elements_page):
    disappearing_elements = Disappearing_elements_page()

    def test_verify_click_home(self):
        self.disappearing_elements.verify_click_home()

    def test_verify_click_about(self):
        self.disappearing_elements.verify_click_about()

    def test_verify_click_contact_us(self):
        self.disappearing_elements.verify_click_contact_us()

    def test_verify_click_portofolio(self):
        self.disappearing_elements.verify_click_portofolio()
