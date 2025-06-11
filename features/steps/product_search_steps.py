from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Go to Target homepage')
def open_site(context):
    context.driver.get('https://www.target.com/')

@when('the user enters {item} in the search bar')
def search_item(context, item):
    context.driver.find_element(By.ID, 'search').send_keys(item)


@when('clicks the search button')
def click_button(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@then('verify search results for "laptop" displayed')
def verify_search(context):
    actual_result = context.driver.find_element(By.XPATH, '//div[./span[contains(text(), "laptop")]]').text
    expected_result = 'laptop'
    assert expected_result in actual_result, f"Expected {expected_result} got {actual_result}"



