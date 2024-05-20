from behave import *
from features.pages.HomePage import HomePage


@given(u'Click on say "{pat_link}" in the left menu bar')
def step_impl(context, pat_link):
    context.home_page = HomePage(context.driver)
    context.home_page.verify_quality_and_pat_text("Quality & PAT")
    context.home_page.click_quality_and_pat_heading()