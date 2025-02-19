from behave import given, when
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_model.base_page import BasePage
from highlight_elements import HighlightElements


@given("The user is logged in the application")
def step_impl(context):
    username = BasePage.user_menu(context)
    HighlightElements.highlight(context, username)
    assert username.text == 'UBS Demo', "Username is incorrect"


@when("The user clicks the 'Offerings' on the top menu")
def step_impl(context):
    offerings_top_menu = BasePage.top_nav_offerings(context)
    HighlightElements.highlight(context, offerings_top_menu)
    offerings_top_menu.click()


@when("The user hovers over 'Payments' in the top menu")
def step_impl(context):
    payments_top_menu = BasePage.top_nav_payments(context)
    HighlightElements.highlight(context, payments_top_menu)
    ActionChains(context.driver).move_to_element(payments_top_menu).perform()
    WebDriverWait(context.driver, 10).until(expected_conditions.visibility_of(BasePage.payments_menu(context)))


@when("The user clicks the 'Account transfer' on the Payments menu")
def step_impl(context):
    acc_trsf_menu = BasePage.acc_transfer(context)
    HighlightElements.highlight(context, acc_trsf_menu)
    acc_trsf_menu.click()
