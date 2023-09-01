from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

COLORS = (By. CSS_SELECTOR, "[class*='desktop-configurator-dim-row']")
CURRENT_COLOR = (By. CSS_SELECTOR, "[id*='text-color_name'][class*='a-size-base']")


@then('Verify User can select colors')
def select_colors(context):
    expected_colors = ['Black', 'Army Green', 'Beige', 'Dark Grey', 'Khaki', 'Light Grey', 'Navy Blue', 'Pink']
    actual_colors = []

    colors = context.driver.find_elements(*COLORS)

    for color in colors[:]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print(current_color)
        actual_colors.append(current_color)

    print(actual_colors)

    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
    print('Test Passed')




