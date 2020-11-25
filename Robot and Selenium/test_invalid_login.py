import os
import unittest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager


class TestInvalidLogin(unittest.TestCase):
    URL = 'https://hedonisticopportunist.github.io/framework_tests/login.html'

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_invalid_login(self):
        self.driver.get(self.URL)
        self.assertTrue('Login 💀' == self.driver.title)
        self.driver.find_element_by_id('username').send_keys('')
        self.driver.find_element_by_id('password').send_keys('')
        self.driver.find_element_by_id('login-form-submit').click()

        err_msg = self.driver.find_element_by_id('login-error-msg').text
        # self.assertFalse(err_msg.strip(), 'Invalid username and/or password'.strip())
        self.assertFalse('Dashboard 💀' == self.driver.title)

    def tearDown(self):
        try:
            self.driver.quit()
        except WebDriverException:
            os.system("taskkill /F /IM chromedriver.exe")
