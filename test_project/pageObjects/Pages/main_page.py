from selenium.webdriver.common.by import By
from test_project.pageObjects.Pages.base_page import BasePage


class MainPage(BasePage):
    _login_link = {"by": By.LINK_TEXT, "value": "Form Authentication"}
    _alert_link = {"by": By.LINK_TEXT, "value": "JavaScript Alerts"}

    def __init__(self, driver):
        self.driver = driver

    def go_login(self):
        self._click(self._login_link)

    def go_alerts_page(self):
        self._click(self._alert_link)