from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_BUTTON = (By.CSS_SELECTOR, "#nav-cart")


@when('Click on Return and Orders icon')
def click_search_icon(context):
    context.driver.find_element(By.ID, "nav-orders").click()
    sleep(1)


@then('Verify Sign in page opened')
def verify_signin(context):
    assert 'signin' in context.driver.current_url.lower()
    assert context.driver.find_element(By.CSS_SELECTOR, ".a-spacing-small").text
    assert context.driver.find_element(By.CSS_SELECTOR, ".a-input-text.a-span12").is_displayed()


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_BUTTON).click()
    sleep(1)


@then('Verify cart is empty')
def empty_cart(context):
    assert 'empty' in context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']").text
