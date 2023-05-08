from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Smolensk")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    # получаем путь к директории текущего исполняемого скрипта lesson2.2_7.py

    file_name = "Doc1.txt"
    # имя файла, который будем загружать на сайт

    file_path = os.path.join(current_dir, file_name)
    # получаем путь к Doc1.txt

    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # отправляем файл
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла