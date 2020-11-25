import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):
    URL = 'https://hedonisticopportunist.github.io/framework_tests/login.html'

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_successful_login(self):
        self.driver.get(self.URL)
        self.assertTrue('Login 💀' == self.driver.title)
        self.driver.find_element_by_id('username').send_keys('user')
        self.driver.find_element_by_id('password').send_keys('holden')
        self.driver.find_element_by_id('login-form-submit').click()
        self.assertTrue('Dashboard 💀' == self.driver.title)

    def tearDown(self):
        self.driver.close()



