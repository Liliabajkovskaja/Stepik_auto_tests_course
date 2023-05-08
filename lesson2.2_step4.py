from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    #print(x)

    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)
 #   print(y)



    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input2 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    input3.click()
    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit.click()



    # Отправляем заполненную форму
   # button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
   # button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
   # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
   # welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()