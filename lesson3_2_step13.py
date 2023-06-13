#import unittest

#class TestHomeWork(unittest.TestCase):
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time




class TestHome(unittest.TestCase):
    def test_link1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()

        browser.get(link1)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block  .form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block  .form-control.second')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block  .form-control.third')
        input3.send_keys("Smolensk")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        needed_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, needed_text)
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Congratulations! You have successfully registered!" == welcome_text

        browser.quit()
    def test_link2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block  .form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block  .form-control.second')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block  .form-control.third')
        input3.send_keys("Smolensk")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        needed_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, needed_text)
        browser.quit()
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # закрываем браузер после всех манипуляций


if __name__ == "__main__":
    unittest.main()