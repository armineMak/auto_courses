class MainPageLinks(object):
    link_for_homepage = "Form Authentication"
    link_for_alerts = "JavaScript Alerts"
    link_for_dropdown = "Dropdown"


class LoginPageLocators(object):
    username_field = "username"
    password_field = "password"
    login_button = "button"
    success_message_displayed = ".flash.success"
    login_area_failure_message = ".flash.error"


class SecureAreaLocators(object):
    logout_submit_button = ".button.secondary"


class AlertsPage(object):
    alert_first_button = '//*[@id="content"]/div/ul/li[1]/button'
    alert_result_text = "result"


class PageDropDown(object):
    drop_down = "dropdown"
    drop_down_option_text = '//*[@id="dropdown"]/option[2]'