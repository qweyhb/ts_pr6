from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome()
browser.get('http://localhost:3000/')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[1]/div/button')
button.click()
time.sleep(5)

email=browser.find_element(by=By.XPATH, value='//*[@id="Mail"]')
email.send_keys('ekaterina_katkova0707@mail.ru')
time.sleep(1)

fullname=browser.find_element(by=By.XPATH, value='//*[@id="Full_name"]')
fullname.send_keys('Ekaterina')
time.sleep(1)

phone=browser.find_element(by=By.XPATH, value='//*[@id="Phone_number"]')
phone.send_keys('123456789')
time.sleep(1)

password=browser.find_element(by=By.XPATH, value='//*[@id="Password"]')
password.send_keys('A1111111')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div/form/button')
button.click()
time.sleep(5)
alert_text = Alert(browser).text
try:
    assert "Регистрация прошла успешно" == alert_text
        print('Тест прошел удачно') 
    except Exception as err:
        print('Тест прошел неудачно')

#Закрываем браузер
browser.close()
