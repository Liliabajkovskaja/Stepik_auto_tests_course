from  selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Vasia")
    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Petrov")
    mail = browser.find_element(By.NAME, "email")
    mail.send_keys("la-la")

    current_dir = os.path.abspath(os.path.dirname(__file__))
# получаем путь к директории текущего исполняемого скрипта lesson2.2_7.py
    file_name = "Doc1.txt"
# имя файла, который будем загружать на сайт
    file_path = os.path.join(current_dir, file_name)
# получаем путь к Doc1.txt
    element = browser.find_element(By.CSS_SELECTOR,"[type='file']" )
# отправляем файл
    element.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

