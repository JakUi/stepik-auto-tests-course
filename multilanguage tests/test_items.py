from selenium import webdriver
import time

def test_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30.0)
    add_2_cart = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket") #Find "Add to cart" button
    assert add_2_cart != None, 'Add to Cart button not found'
