import time
import random
from faker import Faker
from behave import *
from features.pages.HomePage import HomePage
from features.pages.PatRulePage import PatRulePage


@given(u'Click on "{text}" in the left menu bar')
def step_impl(context, text):
    context.home_page = HomePage(context.driver)
    context.home_page.verify_quality_and_pat_text(text)
    context.home_page.click_quality_and_pat_heading()
    time.sleep(2)


@when(u'Click on "{text}"')
def step_impl(context, text):
    context.home_page.click_pat_heading()
    time.sleep(2)
    context.home_page.click_pat_rule_heading()


@when(u'Click "{text}" button from PAT Rules window')
def step_impl(context, text):
    context.pat_rule_page = PatRulePage(context.driver)
    time.sleep(2)
    context.pat_rule_page.click_new_static_pat_link()
    time.sleep(5)


@when(u'Create PAT Rule window will be open and enter rule name as "{name}" and description in "{text}" tab')
def step_impl(context, name, text):
    context.pat_rule_page.click_on_general_tab()
    fake = Faker()
    context.rule_name = fake.name()
    context.pat_rule_page.enter_into_name_field(context.rule_name)


@when(u'Navigate into the parameters tab and select "{text}" as "{Facility}"')
def step_impl(context, text, Facility):
    context.pat_rule_page.click_on_parameters_tab()
    context.pat_rule_page.click_on_facility_option()
    time.sleep(2)


@when(u'After selecting "{text}" data will be populated automatically for work center, device and test program')
def step_impl(context, text):
    context.pat_rule_page.click_on_workcenter_option()
    context.pat_rule_page.click_on_device_option()
    context.pat_rule_page.click_on_testprogram_option()
    time.sleep(5)


@when(u'Select the "{Parameter_Number}"')
def step_impl(context, Parameter_Number):
    context.driver.execute_script("window.scrollBy(0,document.body.scrollWidth);")
    context.pat_rule_page.click_on_parameternumber_option()


@when(u'Keep default settings for "{text}" check box')
def step_impl(context, text):
    assert context.pat_rule_page.verify_validate_pat_limits_checkbox_display()


@when(u'Select Bin Type from drop down')
def step_impl(context):
    context.pat_rule_page.select_bin_type_option("Hard Bin")


@when(u'Navigate to the "Static Limits" tab and enter value for as "{Low_Seed_Limit}" and  as "{High_Seed_Limit}"')
def step_impl(context, Low_Seed_Limit, High_Seed_Limit):
    context.pat_rule_page.click_on_static_limit_tab()
    context.pat_rule_page.enter_into_low_seed_limit_field(Low_Seed_Limit)
    context.pat_rule_page.enter_into_high_seed_limit_field(High_Seed_Limit)


@when(u'Click on the "{text}" button')
def step_impl(context,text):
    context.pat_rule_page.click_on_calculate_seed_button()


@when(u'Create PAT Rule window will open after clicking "{text}" button and available Lots will appear')
def step_impl(context,text):
    time.sleep(2)
    assert context.pat_rule_page.verify_lots_number_display()


@when(u'Select Lot and click "Calculate" button')
def step_impl(context):
    context.pat_rule_page.select_lot_option("73631")
    context.pat_rule_page.click_on_lots_calculate_button()
    time.sleep(5)


@when(u'Value for "{Low_Seed_Limit}" and "{High_Seed_Limit}" will be calculated automatically')
def step_impl(context, Low_Seed_Limit, High_Seed_Limit):
    assert context.pat_rule_page.verify_lots_field_display()


@when(u'Enter the lot number for "{After_Every_Lots}"')
def step_impl(context, After_Every_Lots):
    context.pat_rule_page.enter_into_after_every_lot_field(After_Every_Lots)


@when(u'Provide the "{Value_of_K}"')
def step_impl(context, Value_of_K):
    context.pat_rule_page.enter_into_value_of_k_field(Value_of_K)


@when(u'Select option from "{PAT_limit_to_Apply}" dropdown')
def step_impl(context, PAT_limit_to_Apply):
    context.pat_rule_page.select_pat_limit_to_apply(PAT_limit_to_Apply)


@when(u'Provide "{hard_bin_lower_pat_limit}" and "{soft_bin_lower_pat_limit}"')
def step_impl(context, hard_bin_lower_pat_limit, soft_bin_lower_pat_limit):
    context.pat_rule_page.enter_into_hard_bin_lower_pat_limit(hard_bin_lower_pat_limit)
    context.pat_rule_page.enter_into_soft_bin_lower_pat_limit(soft_bin_lower_pat_limit)


@when(u'Then provide the "{hard_bin_upper_pat_limit}" and "{soft_bin_upper_pat_limit}"')
def step_impl(context, hard_bin_upper_pat_limit, soft_bin_upper_pat_limit):
    context.pat_rule_page.enter_into_hard_bin_upper_pat_limit(hard_bin_upper_pat_limit)
    context.pat_rule_page.enter_into_soft_bin_upper_pat_limit(soft_bin_upper_pat_limit)


@when(u'Click "{Save}" button')
def step_impl(context, Save):
    context.pat_rule_page.click_on_save_button()
    time.sleep(5)
    context.pat_rule_page.verify_newly_created_pat_rule_name(context.rule_name)
