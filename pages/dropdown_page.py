
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Dropdown_page(unittest.TestCase):
    DROPDOWN = (By.ID, "dropdown")
    chrome = webdriver.Chrome()

    def setUp(self):
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/dropdown')
        self.chrome.implicitly_wait(7)

    def tearDown(self):
        self.chrome.quit()

    def select_first_option(self):
        dropdown_element = Select(self.chrome.find_element(*self.DROPDOWN))
        dropdown_element.select_by_visible_text("Option 1")
        selected_option = dropdown_element.first_selected_option.text
        expected_option = "Option 1"
        self.assertEqual(selected_option, expected_option)

    def select_second_option(self):
        dropdown_element = Select(self.chrome.find_element(*self.DROPDOWN))
        dropdown_element.select_by_visible_text("Option 2")
        selected_option = dropdown_element.first_selected_option.text
        expected_option = "Option 2"
        self.assertEqual(selected_option, expected_option)


