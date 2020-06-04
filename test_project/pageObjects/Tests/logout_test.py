import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as Chrome

from test_project.pageObjects.Pages import logout_page


class TestLogout():
    @pytest.fixture
    def logout(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'drivers', 'chromedriver')
        if os.path.isfile(_chromedriver):
            _service = Chrome(executable_path=_chromedriver)
            driver_ = webdriver.Chrome(service=_service)

        else:
            driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return logout_page.LogoutPage(driver_)

    def test_valid(self, logout):
        logout.with_("tomsmith", "SuperSecretPassword!")
        time.sleep(2)
        assert (logout.success_message())

