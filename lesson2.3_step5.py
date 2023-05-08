import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    submit.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window) #переход на новую вкладку

    x_elem = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_elem.text

    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

    print(browser.switch_to.alert.text)



finally:
    time.sleep(5)
    browser.quit()
