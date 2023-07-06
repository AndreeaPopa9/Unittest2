import random
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Key_presses_page(unittest.TestCase):
    INPUT_FIELD = (By.ID, "target")
    RESULT = (By.ID, "result")

    chrome = webdriver.Chrome()

    def setUp(self):
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/key_presses')
        self.chrome.implicitly_wait(7)

    def tearDown(self):
        self.chrome.quit()

    def enter_number(self):
        input_field = self.chrome.find_element(*self.INPUT_FIELD)
        random_numbers = [str(random.randint(1, 5))]
        input_field.send_keys(''.join(random_numbers))
        self.assertEqual(input_field.get_attribute("value"), ''.join(random_numbers))

        #input_field = self.chrome.find_element(*self.INPUT_FIELD)
        #random_number = random.randint(1, 5)
        #input_field.send_keys(str(random_number))
        #self.assertEqual(input_field.get_attribute("value"), str(random_number))

    def enter_keys(self):
        input_field = self.chrome.find_element(*self.INPUT_FIELD)
        input_field.send_keys(Keys.SHIFT)
        actual_result = self.chrome.find_element(*self.RESULT).text
        expected_result = "You entered: SHIFT"
        self.assertEqual(actual_result, expected_result, f"The answer is {actual_result} but it should have been {expected_result}")

    def enter_multiple_keys(self):
        input_field = self.chrome.find_element(*self.INPUT_FIELD)
        num_keys = random.randint(1, 7)
        keys = [Keys.SHIFT, Keys.ALT, Keys.CONTROL, Keys.LEFT, Keys.RIGHT, Keys.UP, Keys.DOWN]
        random_keys = random.choices(keys, k=num_keys)
        for key in random_keys:
            input_field.send_keys(key)
        result = self.chrome.find_element(*self.RESULT).text
        self.assertNotEqual(result, "No keys were entered.")


