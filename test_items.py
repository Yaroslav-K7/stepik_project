import time


def test_find_a_button_add_to_basket(browser):
    """function finding a button add to basket"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    button_basket = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))

    assert button_basket > 0, "Button not found"

    time.sleep(30)
