import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestLoginNonHeadless(unittest.TestCase):
    URL = 'https://hedonisticopportunist.github.io/framework_tests/login.html'

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_successful_login(self):
        # get url and assert that the title is correct
        self.driver.get(self.URL)
        self.assertTrue('Login 💀' == self.driver.title)

        # find the login and password elements and key in user details
        self.driver.find_element_by_id('username').send_keys('user')
        self.driver.find_element_by_id('password').send_keys('holden')
        self.driver.find_element_by_id('login-form-submit').click()

        # verify the page header is 'Dashboard'
        self.assertTrue('Dashboard 💀' == self.driver.title)

        # verify that the puppet h1 text is present
        h1_text = self.driver.find_element_by_tag_name('h1').text
        self.assertTrue(h1_text == 'Muppet Musical :P')

    def tearDown(self):
        self.driver.close()
