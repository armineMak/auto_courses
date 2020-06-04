from selenium.webdriver.common.by import By


class LogoutPage():
    _username_input = {"by": By.ID, "value": "username"}
    _password_input = {"by": By.ID, "value": "password"}
    _submit_button = {"by": By.CSS_SELECTOR, "value": "button"}
    _success_message = {"by": By.CSS_SELECTOR, "value": ".flash.success"}
    _logout_button = {"by": By.CSS_SELECTOR, "value": ".button.secondary"}

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://the-internet.herokuapp.com/login")

    def with_(self, username, password):
        self.driver.find_element(self._username_input["by"],
                                 self._username_input["value"]).send_keys(username)
        self.driver.find_element(self._password_input["by"],
                                 self._password_input["value"]).send_keys(password)
        self.driver.find_element(self._submit_button["by"],
                                 self._submit_button["value"]).click()
        self.driver.find_element(self._logout_button["by"],
                                 self._logout_button["value"]).click()

    def success_message(self):
        return self.driver.find_element(
            self._success_message["by"], self._success_message["value"]).is_displayed()
