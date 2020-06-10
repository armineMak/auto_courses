from selenium.webdriver.common.by import By


class SecurePage():
    _logout_button = {"by": By.CSS_SELECTOR, "value": ".button.secondary"}
    _logout_message = {"by": By.CSS_SELECTOR, "value": ".flash.success"}

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://the-internet.herokuapp.com/secure")

    def button_with_(self):
        self.driver.find_element(self._submit_button["by"],
                                 self._submit_button["value"]).click()

    def logout_message(self):
        return self.driver.find_element(
            self._logout_message["by"], self._logout_message["value"]).isdisplayed()
