import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
dressElement = driver.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div')
driver.execute_script("arguments[0].scrollIntoView();", dressElement)
hover = ActionChains(driver).move_to_element(dressElement).perform()
itemElement = driver.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div/div[2]/h5/a').text
print(itemElement)
dressElement.click()
time.sleep(2)
singleItemElement = driver.find_element_by_xpath('//div[3]/h1').text
print(singleItemElement)
assert itemElement == singleItemElement

driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://automationpractice.com/index.php")
# dressElement = driver.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div')
# driver.execute_script("arguments[0].scrollIntoView();", dressElement)
# hover = ActionChains(driver).move_to_element(dressElement).perform()
# itemElement = driver.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div/div[2]/h5/a').text
# print(itemElement)
# dressElement.click()
# time.sleep(2)
# singleItemElement = driver.find_element_by_xpath('//div[3]/h1').text
# print(singleItemElement)
# assert itemElement == singleItemElement
#
# driver.quit()



