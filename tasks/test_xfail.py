import pytest
import time
import math
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, links):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)
    time.sleep(2)
    browser.find_element_by_tag_name("textarea").send_keys(str(answer))
    time.sleep(2)
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(2)
    correct = browser.find_element_by_class_name("smart-hints__hint").text
    assert correct == "Correct!"
