from selenium.webdriver.common.by import By
from test_project.pageObjects.Pages.base_page import BasePage


class SecurePage(BasePage):
    _logout_button = {"by": By.CSS_SELECTOR, "value": ".button.secondary"}
    _logout_message = {"by": By.CSS_SELECTOR, "value": ".flash.success"}

    def __init__(self, driver):
        self.driver = driver

    def button_with_(self):
        self._click(self._logout_button)

    def logout_message(self):
        return self._is_displayed(self._logout_message)
