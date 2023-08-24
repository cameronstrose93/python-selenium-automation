from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BEST_SELLER = (By.CSS_SELECTOR, "[href*='nav_cs_bestsellers']")
FIVE_LINKS = (By. CSS_SELECTOR, "[class*='all_style_zg-tabs-li-")


@when('Click on BestSeller Button')
def click_bestsellers_icon(context):
    context.driver.find_element(*BEST_SELLER).click()
    sleep(2)


@then('Verify there are Five Links')
def verify_five_links(context):
    links = context.driver.find_elements(*FIVE_LINKS)
    print(links)
    print(f'Total links: {len(links)}')
