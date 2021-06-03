
from selenium import webdriver
import math
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    button_x = browser.find_element_by_id('treasure')
    x = button_x.get_attribute('valuex')
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_class_name('btn').click()
finally:
    time.sleep(10)
    browser.quit()


