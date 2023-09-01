from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_BAR = (By.CSS_SELECTOR, "#twotabsearchtextbox")
SEARCH_BUTTON = (By. CSS_SELECTOR, "#nav-search-submit-button")
CLICK_PRODUCT = (By.CSS_SELECTOR, "[data-asin='B07MW3DG5M']")
ADD_TO_CART = (By.CSS_SELECTOR, "#add-to-cart-button")
NO_COVERAGE = (By.CSS_SELECTOR, "[aria-labelledby='attachSiNoCoverage-announce']")
NUM_ITEMS = (By.ID, "sc-subtotal-label-buybox")
ITEM_IN_CART = (By.CSS_SELECTOR, ".a-truncate-cut")


@when('Search For {product}')
def search_bar(context, product):
    context.driver.find_element(*SEARCH_BAR).send_keys(product)
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BUTTON)).click()


@then('Click on Product')
def click_product(context):
    context.driver.find_element(*CLICK_PRODUCT).click()
    sleep(2)


@then('Add Product to Cart')
def add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART)).click()


@then('Click No Coverage')
def no_coverage(context):
    context.driver.wait.until(EC.element_to_be_clickable(NO_COVERAGE)).click()
    sleep(2)


@then('Verify that 1 item is in the Cart')
def one_in_cart(context):
    expected = '1'
    actual = context.driver.wait.until(EC.presence_of_element_located(NUM_ITEMS)).text
    assert expected in actual, f"Expected query not in {actual}"


@then('Verify that item is in the cart')
def item_in_cart(context):
    expected = 'Cat Calming Diffuser'
    actual = context.driver.wait.until(EC.presence_of_element_located(ITEM_IN_CART)).text
    assert expected in actual, f"Expected query not in {actual}"
    print('Test Passed')