import unittest
from selenium import webdriver
from test_project.pageObjects.Pages.main_page import MainPage
from test_project.pageObjects.Pages.js_alerts_page import JSAlerts


class AlertsAssert(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://the-internet.herokuapp.com/")

    def tearDown(self):
        self.driver.quit()

    def test_js_alert(self):
        main_page = MainPage(self.driver)
        main_page.go_alerts_page()

        alerts_page = JSAlerts(self.driver)
        alerts_page.button1_alert_()

        js_alert = self.driver.switch_to.alert
        js_alert.accept()

        assert alerts_page.alert_message()
