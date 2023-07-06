import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Disappearing_elements_page(unittest.TestCase):
    HOME = (By.XPATH, "//*[@class='example']/ul/li[1]/a")
    ABOUT = (By.XPATH, "//*[@class='example']/ul/li[2]/a")
    CONTACT_US = (By.XPATH, "//*[@class='example']/ul/li[3]/a")
    PORTOFOLIO = (By.XPATH, "//*[@class='example']/ul/li[4]/a")
    TEXT_MESSAGE = (By.XPATH, "//h1[contains(text(),'Not Found')]")

    chrome = webdriver.Chrome()

    def setUp(self):
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/disappearing_elements')
        self.chrome.implicitly_wait(7)

    def tearDown(self):
        self.chrome.quit()

    def verify_click_home(self):
        self.chrome.find_element(*self.HOME).click()
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/"
        assert actual_url == expected_url, f'Invalid url: {actual_url} is different of {expected_url}'

    def verify_click_about(self):
        self.chrome.find_element(*self.ABOUT).click()
        actual = self.chrome.find_element(*self.TEXT_MESSAGE).text
        expected = "Not Found"
        self.assertTrue(expected in actual, "Text message is incorrect")

    def verify_click_contact_us(self):
        self.chrome.find_element(*self.CONTACT_US).click()
        text_element = self.chrome.find_element(*self.TEXT_MESSAGE)
        self.assertTrue(text_element.is_displayed())
        self.assertEqual(text_element.text, "Not Found")

    def verify_click_portofolio(self):
        self.chrome.find_element(*self.PORTOFOLIO).click()
        text_element = self.chrome.find_element(*self.TEXT_MESSAGE)
        self.assertIsNotNone(text_element)








