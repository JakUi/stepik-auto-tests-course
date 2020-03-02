from selenium import webdriver

def test_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    add_2_cart = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert add_2_cart != None, 'Add to Cart button not found'
