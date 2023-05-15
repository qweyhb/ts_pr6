from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome()
browser.get('http://localhost:3000/team')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="basic-navbar-nav"]/div/a[1]')
button.click()
time.sleep(2)

button=browser.find_element(by=By.XPATH, value='//*[@id="basic-navbar-nav"]/div/a[2]')
button.click()
time.sleep(2)

try:
    assert "Услуги" in browser.title
        print('Тест прошел удачно') 
    except Exception as err:
        print('Тест прошел неудачно')

#Закрываем браузер
browser.close()