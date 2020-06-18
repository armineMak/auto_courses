from selenium.webdriver.common.by import By
from test_project.pageObjects.Pages.base_page import BasePage
from test_project.pageObjects.Locators import MainPageLinks


class MainPage(BasePage):
    _login_link = {"by": By.LINK_TEXT, "value": MainPageLinks.link_for_homepage}
    _alert_link = {"by": By.LINK_TEXT, "value": MainPageLinks.link_for_alerts}
    _drop_down_link = {"by": By.LINK_TEXT, "value": MainPageLinks.link_for_dropdown}

    def __init__(self, driver):
        self.driver = driver

    def go_login(self):
        self._click(self._login_link)

    def go_alerts_page(self):
        self._click(self._alert_link)

    def go_dropdown_page(self):
        self._click(self._drop_down_link)