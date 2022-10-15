import time
from cgitb import text

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(5)
    btn = browser.find_element(By.CLASS_NAME, 'btdn-add-to-basket')
    assert btn, NoSuchElementException
    
if __name__ == '__main__':
    pytest.main()










