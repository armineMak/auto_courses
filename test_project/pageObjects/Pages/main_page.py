from selenium.webdriver.common.by import By
from test_project.pageObjects.Pages.login_page import LoginPage
from test_project.pageObjects.Pages.base_page import BasePage


class MainPage(BasePage):
    _login_link = {"by": By.LINK_TEXT, "value": "Form Authentication"}

    def __init__(self, driver):
        self.driver = driver

    def go_login(self):
        self._click(self._login_link)