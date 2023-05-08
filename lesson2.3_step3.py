from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()  #Нажать на кнопку

    confirm = browser.switch_to.alert
    confirm.accept()  #принять конфирм


#На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text

    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

    print(browser.switch_to.alert.text)


finally:
    time.sleep(10)
    browser.quit()