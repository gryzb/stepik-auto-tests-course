import pytest
import unittest
from selenium import webdriver
import time


class TestForm(unittest.TestCase):
    def test_reg1(self):

            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            browser.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[1]/input').send_keys('Ivan')
            browser.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[2]/input').send_keys('Ivanov')
            browser.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[3]/input').send_keys('1@m.as')
            browser.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[1]/input').send_keys('322')
            browser.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[2]/input').send_keys('1@m.as')
            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', "Ok")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[1]/input').send_keys('Ivan')
        browser.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[2]/input').send_keys('Ivanov')
        browser.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[3]/input').send_keys('1@m.as')
        browser.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[1]/input').send_keys('322')
        browser.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[2]/input').send_keys('1@m.as')
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', "Ok")

if __name__ == "__main__":
    unittest.main()
