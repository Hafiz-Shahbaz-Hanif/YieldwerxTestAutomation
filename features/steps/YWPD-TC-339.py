import time

from behave import *
from features.pages.HomePage import HomePage
from features.pages.PatRulePage import PatRulePage


@given(u'Click on say "{pat_link}" in the left menu bar')
def step_impl(context, pat_link):
    context.driver.implicitly_wait(5)
    context.home_page = HomePage(context.driver)
    context.home_page.verify_quality_and_pat_text("Quality & PAT")
    context.home_page.click_quality_and_pat_heading()


@when(u'Click on PAT Rules')
def step_impl(context):
    context.home_page.click_pat_heading()
    context.home_page.click_pat_rules_heading()

@when(u'Click "{text}" button from PAT Rules window')
def step_impl(context, text):
    context.pat_rule_page = PatRulePage(context.driver)
    context.pat_rule_page.click_on_pat_rule_window()