from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target login page')
def open_target_login_page(context):
    context.driver.get('https://www.target.com/')


@when('Click on account icon')
def click_account_button(context):
    context.driver.find_element(By.ID, 'account-sign-in').click()
    sleep(3)

@when('click on side nav sign in button')
def click_side_nav_button(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(3)

@when('user enters valid email')
def enter_email(context):
    context.driver.find_element(By.ID, 'username').send_keys('shuchitadey@yahoo.com')
    context.driver.find_element(By.ID, 'login').click()
    sleep(3)

@when('user enters valid password')
def enter_password(context):
    context.driver.find_element(By.ID, 'password').send_keys('@PyC3Qk!5#GdEa')
    sleep(3)

@when('clicks the sign in button')
def click_sign_in_button(context):
    context.driver.find_element(By.ID, 'login').click()
    sleep(5)
    context.driver.find_element(By.ID, "account-sign-in").click()
    sleep(3)

@then('the user should be logged in successfully')
def verify_user(context):
    actual_result = context.driver.find_element(By.XPATH,'//h2[contains(text(), "Shuchita")]').text
    expected_result = 'Hi, Shuchita'
    assert expected_result in actual_result, f"Expected {expected_result} got {actual_result}"




