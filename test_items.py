import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from cgitb import text
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    btn = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert btn, 'Add to cart button missing'
    
if __name__ == '__main__':
    pytest.main()










