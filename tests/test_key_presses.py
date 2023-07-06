from pages.key_presses_page import Key_presses_page


class Key_presses(Key_presses_page):
    key = Key_presses_page()

    def test_enter_number(self):
        self.key.enter_number()

    def test_enter_keys(self):
        self.key.enter_keys()

    def test_enter_multiple_keys(self):
        self.key.enter_multiple_keys()