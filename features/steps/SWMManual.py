import time

from behave import *

from faker import Faker

from Pages.ActionsPage import ActionsClass
from Pages.DashboardPage import DashboardClass
from Pages.NewSWMManualWindowPage import NewSWMManualClass

actions = ActionsClass()
dc = DashboardClass()
swmm = NewSWMManualClass()


@when('Click "SWM" in the left menu bar')
def step_impl(context):
    dc.click_swm_heading(context)


@when('Click "Manual SWM" and Manual SWM window will open')
def step_impl(context):
    dc.click_manual_swm_policies(context)


@when('Click and select "{source_facility}", the "{source_work_center}", "{source_device}", "{source_test_program}"')
def step_impl(context, source_facility, source_work_center, source_device, source_test_program):
    swmm.click_swm_manual_source_facility(context)
    swmm.click_swm_manual_source_workcenter(context)
    swmm.click_swm_manual_source_device(context)
    swmm.click_swm_manual_source_testprogram(context)


@when('Select Source Lots (73631), Source Wafers (Probe Count = 1)')
def step_impl(context):
    pass


@when('Click and select "{target_facility}", "{target_work_center}", "{target_device}", "{target_test_program}"')
def step_impl(context, target_facility, target_work_center, target_device, target_test_program):
    swmm.click_swm_manual_target_facility(context)
    swmm.click_swm_manual_target_workcenter(context)
    swmm.click_swm_manual_target_device(context)
    swmm.click_swm_manual_target_testprogram(context)


@when('Click and choose "{target_facility}", "{target_work_center}", "{target_device}", "{target_test_program}"')
def step_impl(context, target_facility, target_work_center, target_device, target_test_program):
    swmm.click_swm_manual_target_facility(context)
    swmm.click_swm_manual_target_workcenter(context)
    swmm.click_swm_manual_target_device(context)
    swmm.click_swm_manual_target_testprogram_device_level(context)


@when('Select Target Lots (73631), Target Wafers (Probe Count = 1), "{policies}"')
def step_impl(context, policies):
    pass


@when('Select "Wafer Plotting Option" from "Calculated Wafer/Die Size Settings and Actual Wafer/Die Size Setting"')
def step_impl(context):
    swmm.select_wafer_plotting_option(context, "Calculated Wafer/Die Size Settings")


@when('Click "Generate Manual SWM" button to generate Manual SWM Wafer')
def step_impl(context):
    swmm.click_swm_manual_generate_button(context)


@then('Manual SWM Wafer as Combine Bin Wafer Map with Wafer ID: MC will be generated and be shown')
def step_impl(context):
    swmm.verify_wafer_map_is_displayed(context)
    actions.logout(context)


@when('Click and select Source Facility, the Source Work Center, Source Device, Source Test Program')
def step_impl(context):
    swmm.click_swm_manual_source_facility(context)
    swmm.click_swm_manual_source_workcenter(context)
    swmm.click_swm_manual_source_device(context)
    swmm.click_swm_manual_source_testprogram(context)


@when('Click and select Target Facility, Target Work Center, Target Device, Target Test Program')
def step_impl(context):
    swmm.click_swm_manual_target_facility(context)
    swmm.click_swm_manual_target_workcenter(context)
    swmm.click_swm_manual_target_device(context)
    swmm.click_swm_manual_target_testprogram(context)


@when('Click "Edit Policy" button available top right side of window')
def step_impl(context):
    swmm.click_swm_manual_edit_policy_button(context)


@when('Create SWM Policy window will open and make changes in General, Input Data & Rule selection, Output Data Selection, and Manage exceptions tab that you want to modify')
def step_impl(context):
    swmm.click_swm_manual_edit_policy_output_data_selection_tab(context)
    swmm.select_swm_manual_edit_policy_metadata_selection_form(context, "Target Wafer")
    swmm.click_swm_manual_unselect_source_button(context)
    swmm.click_swm_manual_unselect_target_button(context)


@when('Click "Save" button and Save Change')
def step_impl(context):
    swmm.click_swm_manual_edit_policy_save_btn(context)


@when('After popup appears choose any option and click "OK" button to save the changes')
def step_impl(context):
    swmm.click_swm_manual_policy_ok_btn(context)


@then('Verify that the policy with made changes will be saved and Manual SWM will refresh')
def step_impl(context):
    swmm.verify_wafer_map_is_displayed(context)
    actions.logout(context)


