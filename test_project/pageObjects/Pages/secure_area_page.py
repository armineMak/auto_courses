from selenium.webdriver.common.by import By
from test_project.pageObjects.Pages.base_page import BasePage
from test_project.pageObjects.Locators import SecureAreaLocators
from test_project.pageObjects.Locators import LoginPageLocators


class SecurePage(BasePage):
    _logout_button = {"by": By.CSS_SELECTOR, "value": SecureAreaLocators.logout_submit_button}
    _logout_message = {"by": By.CSS_SELECTOR, "value": LoginPageLocators.success_message_displayed}

    def __init__(self, driver):
        self.driver = driver

    def button_with_(self):
        self._click(self._logout_button)

    def logout_message(self):
        return self._is_displayed(self._logout_message)
