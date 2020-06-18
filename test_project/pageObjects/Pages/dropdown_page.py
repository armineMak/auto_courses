from selenium.webdriver.common.by import By
from test_project.pageObjects.Pages.base_page import BasePage
from test_project.pageObjects.Locators import PageDropDown


class DropdownList(BasePage):
    _select_box = {"by": By.ID, "value": PageDropDown.drop_down}
    _select_option = {"by": By.XPATH, "value": PageDropDown.drop_down_option_text}

    def __init__(self, driver):
        self.driver = driver

    def drop_down_list_(self):
        self._click(self._select_box)

    def option_text_(self):
        return self._is_displayed(self._select_option)

    def click_on_option_(self):
        self._click(self._select_option)