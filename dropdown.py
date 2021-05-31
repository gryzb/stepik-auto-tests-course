
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x = int(browser.find_element_by_id("input_value").text)
    y = calc(x)

    input_field = browser.find_element_by_class_name("form-control")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
    input_field.send_keys(y)

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(10)
    browser.quit()


