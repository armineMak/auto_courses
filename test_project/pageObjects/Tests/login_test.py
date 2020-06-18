import unittest
from selenium import webdriver

from test_project.pageObjects.Pages.main_page import MainPage
from test_project.pageObjects.Pages.login_page import LoginPage
from test_project.pageObjects.Pages.secure_area_page import SecurePage


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://the-internet.herokuapp.com/")

    def tearDown(self):
        self.driver.quit()

    def test_auth_flow(self):
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        secure_area = SecurePage(self.driver)
        logout_page = LoginPage(self.driver)

        main_page.go_login()
        login_page.login_fields_("tomsmith", "SuperSecretPassword!")
        secure_area.button_with_()
        assert login_page.success_message_displayed()


