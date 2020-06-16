import unittest
from selenium import webdriver
from test_project.pageObjects.Pages.main_page import MainPage
from test_project.pageObjects.Pages.dropdown_page import DropdownList


class AlertsAssert(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://the-internet.herokuapp.com/")

    def tearDown(self):
        self.driver.quit()

    def test_drop_down_list(self):
        main_page = MainPage(self.driver)
        main_page.go_dropdown_page()

        drop_down_page = DropdownList(self.driver)
        drop_down_page.drop_down_list_()
        drop_down_page.click_on_option_()
        assert drop_down_page.option_text_()

