import time

from behave import *

from faker import Faker

from Pages.ActionsPage import ActionsClass
from Pages.DashboardPage import DashboardClass
from Pages.NewSWMPolicyWindowPage import NewSWMPolicyClass
from Pages.NewSWMRuleWindowPage import NewSWMRulWindowClass

actions = ActionsClass()
dc = DashboardClass()
swmp = NewSWMPolicyClass()
sw = NewSWMRulWindowClass()


@when('Click on "SWM" in the left menu bar and click on SWM Policies')
def step_impl(context):
    dc.click_swm_heading(context)
    dc.click_swm_policies_heading(context)


@when('Click New SWM Policy button from SWM Policies window')
def step_impl(context):
    swmp.click_new_swm_policy_window(context)


@when('Create SWM Policy Window will open')
def step_impl(context):
    swmp.verify_create_swm_policy_window_display(context, "Create SWM Policy")


@when('Enter "{name}" And description in "General" tab')
def step_impl(context, name):
    fake = Faker()
    context.test_program_level_policy_name = name + fake.name()
    context_description = fake.text()
    sw.enter_into_swm_rule_name_field(context, context.test_program_level_policy_name)
    sw.enter_into_swm_rule_description_field(context, context_description)


@when('Click "Input Data & Rule Selection" And Select "{level}" from dropdown')
def step_impl(context, level):
    swmp.click_input_data_and_rule_selection_tab(context)
    sw.select_level(context, level)


@when('Select "{rules} from the Rules section')
def step_impl(context, rules):
    swmp.select_rules(context)


@when('Click "Output Data Selection" tab and provide all the information like')
def step_impl(context):
    swmp.click_output_data_selection_tab(context)


@when('Enter the information for')
def step_impl(context):
    pass


@when('Enter the information for "Wafer Rotation" like')
def step_impl(context):
    pass


@when('Select Die Type Details by using checkbox')
def step_impl(context):
    swmp.click_select_all_source_dies_button(context)
    swmp.click_select_all_target_dies_button(context)


@when('Click Manage Exception tab and select the required option otherwise keep it as default')
def step_impl(context):
    swmp.click_manage_exceptions_tab(context)


@when('Click Save button to save the new created policy')
def step_impl(context):
    swmp.click_create_policy_save_btn(context)


@then('Verify that the policy has been saved and appears in the SWM Policies window')
def step_impl(context):
    swmp.verify_newly_created_swm_policy_name(context, context.test_program_level_policy_name)
    actions.logout(context)


@when('Select "{test_program_options}" as Custom')
def step_impl(context, test_program_options):
    swmp.click_custom_radio_btn(context)


@when('Select "(1|M)" as a Source Probe')
def step_impl(context):
    sw.click_source_probe(context)


@when('Select the "(1|M)" option as Target Probe')
def step_impl(context):
    sw.click_target_probe(context)


@when('Click on Manage Test Programs Hyperlink and provide Test Programs Mapping')
def step_impl(context):
    swmp.click_manage_test_programs_link(context)


@when('Select Source Test Program and Target Test Program from their respective dropdowns and click Add button')
def step_impl(context):
    swmp.select_policy_source_test_program(context, "PREBAKE_A_4670")
    swmp.select_policy_target_test_program(context, "POSTBAKE_A_4670")
    swmp.click_policy_add_btn(context)


@when('Click Apply button after adding')
def step_impl(context):
    swmp.click_policy_apply_btn(context)


@when('See the list of already created SWM policies')
def step_impl(context):
    swmp.verify_swm_policy_table_is_displayed(context)


@when('Click "Edit" button available for each policy')
def step_impl(context):
    swmp.click_swm_policy_edit_button(context)


@when('Change the "Name" and "Description" in "General" tab')
def step_impl(context):
    fake = Faker()
    context.edited_policy_name = fake.name()
    sw.edit_swm_rule_name_field(context, context.edited_policy_name)


@when('Make changes that you want in tabs')
def step_impl(context):
    swmp.click_create_policy_save_btn(context)
    swmp.click_swm_policy_ok_btn(context)


@then('Verify that the edited policy has been saved and appears in the SWM Policies window')
def step_impl(context):
    swmp.verify_newly_created_swm_policy_name(context, context.edited_policy_name)
    actions.logout(context)


@when('Click Copy button available infront of each already created policy')
def step_impl(context):
    swmp.click_swm_policy_copy_button(context)


@when('Change name and description from in the General tab')
def step_impl(context):
    fake = Faker()
    context.copied_policy_name = fake.name()
    sw.edit_swm_rule_name_field(context, context.copied_policy_name)


@when('Make required changes in tabs')
def step_impl(context):
    swmp.click_input_data_and_rule_selection_tab(context)
    swmp.select_policy_level(context)
    swmp.click_custom_radio_btn(context)
    swmp.select_rules(context)
    swmp.click_manage_test_programs_link(context)
    swmp.select_policy_source_test_program(context, "POSTBAKE_A_4670")
    swmp.select_policy_target_test_program(context, "POSTBAKE_A_4670")
    swmp.click_policy_add_btn(context)
    swmp.click_policy_apply_btn(context)
    swmp.click_create_policy_save_btn(context)


@then('Verify that the copied policy has been saved and appears in the SWM Policies window')
def step_impl(context):
    swmp.verify_newly_created_swm_policy_name(context, context.copied_policy_name)
    actions.logout(context)


@when('Click delete button available at the end of each policy')
def step_impl(context):
    context.deleted_swm_policy_name = swmp.verify_deleted_swm_policy_name(context)
    swmp.click_swm_policy_delete_button(context)


@when('Confirmation Required pop-up window will appear, with "Yes" and "No" buttons')
def step_impl(context):
    swmp.verify_swm_policy_delete_alert_is_displayed(context)


@when('Click "Yes" to delete the policy')
def step_impl(context):
    swmp.accept_swm_policy_delete_alert(context)


@then('Verify that the policy will be deleted')
def step_impl(context):
    sw.verify_swm_rule_delete_success_popup_is_displayed(context)
    swmp.verify_deleted_swm_policy_name_is_removed(context, context.deleted_swm_policy_name)
    actions.logout(context)


@step("Create New Assembly Map Policy as a Pre-Requisite")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Create New Assembly Map Policy as a Pre-Requisite')