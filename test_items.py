import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)

    assert browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary"), 'Button not found'
    time.sleep(30)
