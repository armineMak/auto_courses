from selenium.webdriver.common.by import By
from test_project.pageObjects.Pages.base_page import BasePage


class DropdownList(BasePage):
    _select_box = {"by": By.ID, "value": "dropdown"}
    _select_option = {"by": By.XPATH, "value": '//*[@id="dropdown"]/option[2]'}

    def __init__(self, driver):
        self.driver = driver

    def drop_down_list_(self):
        self._click(self._select_box)

    def option_text(self):
        return self._is_displayed(self._select_option)