from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# create a new Chrome browser instance
service = Service(executable_path='/Users/cameronst.rose/QA/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

"""
# Amazon Logo, By.XPATH, "//i[@class='a-icon a-icon-logo']" 
# Email Field, By.ID, "ap_email"
# Continue Button, By.ID, "continue"
# Conditions of use link, By.XPATH, "//*[@id="legalTextRow"]/a[1]"
# Privacy Notice Link, By.XPATH, "//*[@id='legalTextRow']/a[2]"
# Need Help Link, By.CLASS, "//span[@class='a-expander-prompt']"
# Forgot your password link, By.ID, "auth-fpp-link-bottom"
# Other issues with Sign-In link, By.ID, "ap-other-signin-issues-link"
# Create your Amazon account button, By.ID, "createAccountSubmit"
"""

# open the url
driver.get('https://www.amazon.com/')

# click on order button
driver.find_element(By.ID, 'nav-orders').click()

# Wait 4 seconds
sleep(4)

# verify search results
assert 'Sign in' in driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert driver.find_element(By.ID,"ap_email").is_displayed()
print('Test Passed')
