import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as Chrome

from pageObjects.Pages import login_page


class TestLogin():
    @pytest.fixture
    def login(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'drivers', 'chromedriver')
        if os.path.isfile(_chromedriver):
            _service = Chrome(executable_path=_chromedriver)
            driver_ = webdriver.Chrome(service=_service)

        else:
            driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return login_page.LoginPage(driver_)

    def test_valid(self, login):
        login.with_("tomsmith", "SuperSecretPassword!")
        assert (login.success_message())

    def test_invalid_username(self, login):
        login.with_("toms", "SuperSecretPassword!")
        assert (login.failure_message())

    def test_invalid_password(self, login):
        login.with_("tomsmith", "!%^%$JK")
        assert (login.failure_message())

