from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


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
    context.driver.find_element(By.CSS_SELECTOR, ".nav-cart-icon").click()
    sleep(1)


@then('Verify cart is empty')
def empty_cart(context):
    assert 'empty' in context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']").text
