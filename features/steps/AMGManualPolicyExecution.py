import time

from behave import *

from Pages.AMGManualPolicyExecutionPage import ManualAMGPolicyExecution
from Pages.AMGPickMapPage import AMGManualAssemblyClass
from Pages.ActionsPage import ActionsClass
from Pages.DashboardPage import DashboardClass
from Pages.NewAMGPolicyWindowPage import NewAMGPolicyClass

actions = ActionsClass()
dc = DashboardClass()
amgp = NewAMGPolicyClass()
amg_manual = AMGManualAssemblyClass()
amg_policy_exec = ManualAMGPolicyExecution()


@when('Open Manual AMG Policy Execution')
def step_impl(context):
    dc.click_assembly_map_heading(context)
    dc.click_manual_amg_policy_execution_heading(context)


@when('Select facility data to generate Assembly Maps')
def step_impl(context):
    amgp.click_facility(context)


@when('After selecting the data facility, Work Center, Device, Test Program, Lot, and policy should be selected automatically')
def step_impl(context):
    amg_policy_exec.verify_lot_id_checkbox_is_checked(context)


@when('Select the wafers to generate their Assembly Maps')
def step_impl(context):
    amg_policy_exec.verify_wafer_checkbox_is_checked(context)


@when('Click the Reset Button')
def step_impl(context):
    amg_manual.click_reset_btn(context)


@then('Verify that All the data selections will be reset')
def step_impl(context):
    amg_policy_exec.verify_work_center_is_not_displayed(context)
    actions.logout(context)


@given('Create New Assembly Map Policies as a Pre-Requisite')
def step_impl(context):
    dc.click_assembly_map_heading(context)
    dc.click_assembly_map_policies_heading(context)
    actions.create_new_amg_policy(context)
    actions.create_new_amg_test_program_level_policy(context)


@when('Select "{data_set_size}", and "{facility}" to generate Assembly Maps')
def step_impl(context, data_set_size, facility):
    amgp.click_facility(context)


@when('Choose the Policies of your choice')
def step_impl(context):
    context.data_set = []
    for row in context.table:
        value = row['Policies']
        if row['Policies'] == 'Test Program Level Policy':
            amg_policy_exec.choose_test_program_level_policy(context)
        else:
            amg_policy_exec.choose_device_level_policy(context)


@when('Click on Generate Policy Based Assembly Map')
def step_impl(context):
    amg_policy_exec.click_policy_based_amg_map_btn(context)


@when('Assembly Map Generated Successfully message appears')
def step_impl(context):
    amg_policy_exec.verify_success_popup_is_displayed(context)


@when('Delete the created policies as post-requisite')
def step_impl(context):
    actions.delete_created_amg_policy(context)
    actions.delete_created_amg_policy(context)
    actions.logout(context)

