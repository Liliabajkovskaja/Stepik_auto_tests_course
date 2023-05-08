import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

#    Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#   Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#  Нажать на кнопку "Book"
#Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение


browser  = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

button_book = WebDriverWait(browser,15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")  #   Дождаться, когда цена дома уменьшится до $100, (можно без переменной)
)
book = browser.find_element(By.ID, 'book')
book.click()

x_elem = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_elem.text
y = calc(x)

answer = browser.find_element(By.CSS_SELECTOR, '#answer')
answer.send_keys(y)

button = browser.find_element(By.ID, 'solve')
button.click()

print(browser.switch_to.alert.text)

time.sleep(5)
browser.quit()
