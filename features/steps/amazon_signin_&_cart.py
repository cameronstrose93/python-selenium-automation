from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CART_BUTTON = (By.CSS_SELECTOR, "#nav-cart")
ORDER_BUTTON = (By.CSS_SELECTOR, "#nav-orders")
SIGN_IN_TITLE = (By.CSS_SELECTOR, "[class='a-spacing-small']")
EMAIL_FIELD = (By.CSS_SELECTOR, ".a-input-text.a-span12")
CART_EMPTY_TITLE = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")


@when('Click on Return and Orders icon')
def click_search_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable(ORDER_BUTTON)).click()


@then('Verify Sign in page opened')
def verify_signin(context):
    assert 'signin' in context.driver.current_url.lower()
    assert context.driver.wait.until(EC.presence_of_element_located(SIGN_IN_TITLE)).text
    assert context.driver.wait.until(EC.presence_of_element_located(EMAIL_FIELD)).is_displayed()


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable(CART_BUTTON)).click()


@then('Verify cart is empty')
def empty_cart(context):
    assert 'Your Amazon Cart is empty' in context.driver.wait.until(EC.presence_of_element_located(CART_EMPTY_TITLE)).text
