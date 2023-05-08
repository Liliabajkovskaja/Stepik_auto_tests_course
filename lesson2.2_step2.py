from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    a = x_element.text


    b_element = browser.find_element(By.CSS_SELECTOR, '#num2')
    b = b_element.text

    sum = str(int(a)+int(b))


#select = Select(browser.find_element(By.TAG_NAME, "select"))
#select.select_by_value("sum") # ищем элемент с текстом "Python"

  #  browser.find_element(By.TAG_NAME, "select").click()
   # browser.find_element(By.CSS_SELECTOR, (f"[value='{sum}']")).click()

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)

    submit = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
