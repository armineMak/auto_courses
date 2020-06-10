from selenium.webdriver.common.by import By
from test_project.pageObjects.Pages.base_page import BasePage


class LoginPage(BasePage):
    _username_input = {"by": By.ID, "value": "username"}
    _password_input = {"by": By.ID, "value": "password"}
    _submit_button = {"by": By.CSS_SELECTOR, "value": "button"}
    _success_message = {"by": By.CSS_SELECTOR, "value": ".flash.success"}
    _failure_message = {"by": By.CSS_SELECTOR, "value": ".flash.error"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("http://the-internet.herokuapp.com/login")

    def with_(self, username, password):
        self._type(self._username_input, username)
        self._type(self._password_input, password)
        self._click(self._submit_button)

    def success_message_displayed(self):
        return self._is_displayed(self._success_message, timeout=0)

    def failure_message_displayed(self):
        return self._is_displayed(self._failure_message, timeout=2)