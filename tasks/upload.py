
from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)

    browser.find_element_by_name('firstname').send_keys('Andrew')
    browser.find_element_by_name('lastname').send_keys('Gears')
    browser.find_element_by_name('email').send_keys('1@m.as')

    current_dir = os.path.abspath(os.path.dirname('C:/Users/dekin/PycharmProjects/Test'))
    file_path = os.path.join(current_dir, 'test.txt')
    browser.find_element_by_id('file').send_keys(file_path)
    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(10)
    browser.quit()


