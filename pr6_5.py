from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome()
browser.get('http://localhost:3000/')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="basic-navbar-nav"]/div/a[2]')
button.click()
time.sleep(2)

button=browser.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/form/button')
button.click()
time.sleep(5)
alert_text = Alert(browser).text
try:
    assert "Необходимо данные в обязательные поля" == alert_text
        print('Тест прошел удачно') 
    except Exception as err:
        print('Тест прошел неудачно')

#Закрываем браузер
browser.close()