import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Login_page(unittest.TestCase):

    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
    H2_ELEMENT = (By.XPATH, '//h2')
    HREF_LINK = (By.XPATH, '//a[@href="http://elementalselenium.com/"]')
    USER_NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    ERROR_MESSAGE = (By.XPATH, "//div[(contains(text(),'Your username is invalid'))]")
    ERROR_CLOSED = (By.XPATH, '//a[@class="close"]')
    LABEL_LIST = (By.XPATH, '//label')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="flash success"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')
    ELEM_H4 = (By.XPATH, '//h4[@class="subheader"]')

    chrome = webdriver.Chrome()

    def setUp(self):
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/login')
        self.chrome.implicitly_wait(7)

    def tearDown(self):
        self.chrome.quit()

    def verify_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected,actual, 'URL-ul nu este corect')

    def verify_page_title(self):
        actual = self.chrome.title
        expected='The Internet'
        self.assertEqual(expected, actual,  f' Titlul paginii este {actual}, dar ar fi trebuit sa fie {expected}')

    def verify_element_h2(self):
        actual=self.chrome.find_element(*self.H2_ELEMENT).text
        print(f'Denumirea elementului este {actual}')
        expected='Login Page'
        self.assertEqual(actual, expected, f' Denumirea elementului este {actual}, dar ar fi trebuit sa fie {expected}')

    def verify_href_link(self):
        actual_link=self.chrome.find_element(*self.HREF_LINK).get_attribute('href')
        assert actual_link=='http://elementalselenium.com/', 'Link-ul este gresit'
        print('Link-ul verificat este corect')


    def verify_error_message(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tom')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR_MESSAGE).text
        expected='Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    def verify_close_error_message(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.ERROR_CLOSED).click()
        WebDriverWait(self.chrome, 1).until(EC.invisibility_of_element_located(self.ERROR_MESSAGE))

        try:
            self.chrome.find_element(*self.ERROR_MESSAGE)
            self.fail("The error message is still displayed")
        except NoSuchElementException:
             print("The text is not visible on the page!")

    def verify_label_text(self):
        label_elements = self.chrome.find_elements(By.XPATH, '//label')
        label_texts = [element.text for element in label_elements]
        expected_texts = ["Username", "Password"]
        for i in range(len(expected_texts)):
            self.assertEqual(label_texts[i], expected_texts[i])

    def verify_secure_link(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        url_after_login = self.chrome.current_url
        self.assertTrue("secure" in url_after_login,'The new URL does not contain secure')
        WebDriverWait(self.chrome,10).until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
        assert self.chrome.find_element(*self.SUCCESS_MESSAGE).is_displayed() == True

    def verify_login_logout(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        WebDriverWait(self.chrome,10).until(EC.url_contains('/login'))
        url_after_logout = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        assert url_after_logout == expected_url, f'Invalid url: {url_after_logout} is different of {expected_url}'