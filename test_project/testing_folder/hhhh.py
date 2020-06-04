import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as Chrome


class TestLogin():
    @pytest.fixture
    def driver(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'drivers', 'chromedriver')
        if os.path.isfile(_chromedriver):
            _service = Chrome(executable_path=_chromedriver)
            driver_ = webdriver.Chrome(service=_service)

        else:
            driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return driver_

    def test_inValid_credentials(self, driver):
        driver.get("http://the-internet.herokuapp.com/login")
        driver.find_element(By.ID, "username").send_keys("armine")
        driver.find_element(By.ID, "password").send_keys("makaryan!")
        driver.find_element(By.CSS_SELECTOR, "button").click()
        assert driver.find_element(By.CSS_SELECTOR,
                                   ".flash.error").is_displayed(), "Your username is invalid!"
        time.sleep(2)
        # driver.find_element(By.CSS_SELECTOR, "#content > div > a").click()
        # error_text = driver.find_element(By.CSS_SELECTOR, ".flash.success").text
        # assert error_text == "You logged into b secure area!", "Invalid message for LogIn"
        # assert(driver.find_element(By.CSS_SELECTOR, ".flash.success").is_displayed())
