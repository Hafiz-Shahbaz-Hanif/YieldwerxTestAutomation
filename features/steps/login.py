from behave import *
from features.pages.LoginPage import LoginPage


@given('I navigated to Login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)


@when('I enter valid username and valid password into the fields')
def step_impl(context):
    for row in context.table:
        context.login_page.enter_into_username_field(row["username"])
        context.login_page.enter_into_password_field(row["password"])


@when('I click on Login button')
def step_impl(context):
    context.login_page.click_on_login_button()


@then('I should get logged in')
def step_impl(context):
    assert context.login_page.verify_homepage_heading_text("Realtime SPC Templates")