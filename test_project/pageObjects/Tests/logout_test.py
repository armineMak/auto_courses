import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chrome

from test_project.pageObjects.Pages import login_page
from test_project.pageObjects.Pages import secure_area_page


class TestSecurePage():
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
        assert login.success_message()


