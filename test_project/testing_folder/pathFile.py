from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/login");

username = driver.find_element_by_id("username")
username.send_keys("tomsmith")

password = driver.find_element_by_id("password")
password.send_keys("SuperSecretPassword!")

login = driver.find_element_by_css_selector("#login > button").click()
logout = driver.find_element_by_css_selector("#content > div > a").click()

driver.quit()
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
