from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome()
browser.get('http://localhost:3000/')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="basic-navbar-nav"]/div/a[2]')
button.click()
time.sleep(2)

email=browser.find_element(by=By.XPATH, value='//*[@id="email"]')
email.send_keys('ekaterina_katkova0707@mail.ru')
time.sleep(1)

password=browser.find_element(by=By.XPATH, value='//*[@id="password"]')
password.send_keys('A1111111')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/form/button')
button.click()
time.sleep(5)
alert_text = Alert(browser).text
try:
    assert "Авторизация прошла успешно" == alert_text
        print('Тест прошел удачно') 
    except Exception as err:
        print('Тест прошел неудачно')

#Закрываем браузер
browser.close()