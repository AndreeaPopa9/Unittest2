from pages.login_page import Login_page


class Login(Login_page):
    login = Login_page()


    def test_url(self):
        self.login.verify_url()

    def test_page_title(self):
        self.login.verify_page_title()

    def test_element_h2(self):
        self.login.verify_element_h2()

    def test_href_link(self):
        self.login.verify_href_link()

    def test_error_message(self):
        self.login.verify_error_message()

    def test_close_error_message(self):
        self.login.verify_close_error_message()

    def test_label_text(self):
        self.login.verify_label_text()

    def test_verify_secure_link(self):
        self.login.verify_secure_link()

    def test_login_logout(self):
        self.login.verify_login_logout()