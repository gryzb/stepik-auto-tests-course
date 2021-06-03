import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    browser.find_element_by_css_selector('#book').click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    x = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_id('solve').click()


finally:
    time.sleep(10)
    browser.quit()