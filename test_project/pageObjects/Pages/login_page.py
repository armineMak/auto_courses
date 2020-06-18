from selenium.webdriver.common.by import By
from test_project.pageObjects.Pages.base_page import BasePage
from test_project.pageObjects.Locators import LoginPageLocators


class LoginPage(BasePage):
    _username_input = {"by": By.ID, "value": LoginPageLocators.username_field}
    _password_input = {"by": By.ID, "value": LoginPageLocators.password_field}
    _submit_button = {"by": By.CSS_SELECTOR, "value": LoginPageLocators.login_button}
    _success_message = {"by": By.CSS_SELECTOR, "value": LoginPageLocators.success_message_displayed}
    _failure_message = {"by": By.CSS_SELECTOR, "value": LoginPageLocators.login_area_failure_message}

    def __init__(self, driver):
        self.driver = driver

    def login_fields_(self, username_field, password_field):
        self._type(self._username_input, username_field)
        self._type(self._password_input, password_field)
        self._click(self._submit_button)

    def success_message_displayed(self):
        return self._is_displayed(self._success_message)

    def failure_message_displayed(self):
        return self._is_displayed(self._failure_message)