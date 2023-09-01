from behave import given, when, then
from time import sleep


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(1)
    context.driver.refresh()


@given('Open Amazon Hat Page')
def open_hat_page(context):
    context.driver.get('https://a.co/d/bnhB50Y')
    sleep(1)
    context.driver.refresh()

