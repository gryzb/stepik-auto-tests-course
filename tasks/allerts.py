
from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)
    browser.find_element_by_class_name('btn').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_tag_name('answer').send_keys(calc(x))
    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(10)
    browser.quit()