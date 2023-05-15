from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome()
browser.get('http://localhost:3000/team')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="basic-navbar-nav"]/div/a[3]')
button.click()
time.sleep(2)

button=browser.find_element(by=By.XPATH, value='//*[@id="basic-navbar-nav"]/div/a[6]')
button.click()
time.sleep(2)
alert_text = Alert(browser).text
try:
    assert "Тело достигает того, во что верит разум" == alert_text
        print('Тест прошел удачно') 
    except Exception as err:
        print('Тест прошел неудачно')

#Закрываем браузер
browser.close()