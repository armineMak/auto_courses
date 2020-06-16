from selenium.webdriver.common.by import By
from test_project.pageObjects.Pages.base_page import BasePage


class JSAlerts(BasePage):
    _js_alert_button1 = {"by": By.XPATH, "value": '//*[@id="content"]/div/ul/li[1]/button'}
    _result_text = {"by": By.ID, "value": "result"}

    def __init__(self, driver):
        self.driver = driver

    def button1_alert_(self):
        self._click(self._js_alert_button1)
        js_alert = self.driver.switch_to.alert
        js_alert.accept()

    def alert_message(self):
        return self._is_displayed(self._result_text, timeout=3)
