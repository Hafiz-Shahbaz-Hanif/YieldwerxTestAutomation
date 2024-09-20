import time

from behave import *
from faker import Faker
from Pages.ActionsPage import ActionsClass
from Pages.DashboardPage import DashboardClass
from Pages.NewAMGPolicyWindowPage import NewAMGPolicyClass

actions = ActionsClass()
dc = DashboardClass()
amgp = NewAMGPolicyClass()


@when('Open Assembly Map Policies module')
def step_impl(context):
    dc.click_assembly_map_heading(context)
    dc.click_assembly_map_policies_heading(context)


@when('Click on the Create Assembly Map Policy button')
def step_impl(context):
    amgp.click_create_assembly_map_policy_button(context)


@when('Provide the assembly map policy "{name}" in the "General" tab')
def step_impl(context, name):
    context.test_program_level_amg_policy_name = name
    amgp.enter_into_assembly_policy_name_field(context, context.test_program_level_amg_policy_name)


@when('Navigate into the "Parameter" tab and select the "{data_set_size}", and "{facility}"')
def step_impl(context, data_set_size, facility):
    amgp.navigate_to_parameters_tab(context)
    amgp.click_facility(context)


@when('After selecting facility data will be populated automatically for work center, device and test program')
def step_impl(context):
    pass


@when('Choose wafer from "{generate_assembly_map_from}" dropdown available on the parameters tab')
def step_impl(context, generate_assembly_map_from):
    amgp.select_generate_assembly_map(context, generate_assembly_map_from)


@when('Navigate into the "Generation" tab')
def step_impl(context):
    amgp.navigate_to_generation_tab(context)


@when('Choose the AMG format from "{amg_file_format}" dropdown')
def step_impl(context, amg_file_format):
    amgp.select_conversion_file_format(context, amg_file_format)


@when('Navigate into the "Output" tab')
def step_impl(context):
    amgp.navigate_to_output_tab(context)


@when('Enter the folder path into the "{main_dir}" Input field')
def step_impl(context, main_dir):
    amgp.enter_folder_path(context, main_dir)
    context.output_destination_path = main_dir


@when('Select the options from "{amg_file_exists}"')
def step_impl(context, amg_file_exists):
    amgp.click_amg_map_file_exists_radio_button(context)


@when('Enter the "{file_name_format}" into the input field, Enter @ in the input field, options list will be visible select option from the list')
def step_impl(context, file_name_format):
    amgp.enter_file_name_format(context, file_name_format)


@when('Choose the "{output_path}" from the available Options')
def step_impl(context, output_path):
    amgp.click_local_or_network_drive_radio_button(context)


@when('Click on the "Add Path" button')
def step_impl(context):
    amgp.click_add_path_button(context)


@when('Check on the "Output Destination Of Assembly Map File" that path has been added')
def step_impl(context):
    amgp.verify_output_destination_amg_file_path(context, context.output_destination_path)


@when('Enable the check box of "{save_assembly_map}"')
def step_impl(context, save_assembly_map):
    amgp.check_save_assembly_map_checkbox(context)


@when('Click on the save button available at the end')
def step_impl(context):
    amgp.click_amg_policy_save_button(context)


@when('Saved AMG policy is shown in the AMG Policies grid section')
def step_impl(context):
    amgp.verify_newly_created_amg_policy_name_on_grid(context, context.test_program_level_amg_policy_name)


@when('Enable your saved policy')
def step_impl(context):
    amgp.check_enable_policy_checkbox(context)
    amgp.accept_enable_policy_popup(context)


@then('Policy will be activated successfully')
def step_impl(context):
    amgp.verify_automate_amg_policy_checkbox_is_enabled(context)
    actions.logout(context)


@when('Provide the assembly map device level policy "{name}" in the General tab')
def step_impl(context, name):
    context.device_level_amg_policy_name = name
    amgp.enter_into_assembly_policy_name_field(context, context.device_level_amg_policy_name)


@when('Enable "{apply_amg_policy_to_device_level}" check box')
def step_impl(context, apply_amg_policy_to_device_level):
    amgp.check_apply_amg_policy_to_device_level_checkbox(context)


@when('Saved AMG Device Level policy is shown in the AMG Policies grid section')
def step_impl(context):
    amgp.verify_newly_created_amg_policy_name_on_grid(context, context.device_level_amg_policy_name)


@when('Enable your saved Device Level AMG policy')
def step_impl(context):
    amgp.check_enable_policy_device_level_checkbox(context)
    amgp.accept_enable_policy_popup(context)


@when('Provide assembly map policy name as "{policy_name}" in "General" tab')
def step_impl(context, policy_name):
    context.lot_completion_policy = policy_name
    amgp.enter_into_assembly_policy_name_field(context, context.lot_completion_policy)


@when('Navigate into "Parameter" tab and select the data facility')
def step_impl(context):
    amgp.navigate_to_parameters_tab(context)
    amgp.click_facility(context)


@when('After selecting facility data will be populated automatically for work center, device and test program, for device level test program will be gray out')
def step_impl(context):
    pass


@when('Enable "Apply AMG Policy To Device Level" check box or proceed without enabling this check box for test program level')
def step_impl(context):
    amgp.check_apply_amg_policy_to_device_level_checkbox(context)
    amgp.test_program_is_disabled(context)


@when('Enable "Check for Lot Completion" checkbox')
def step_impl(context):
    amgp.check_for_lot_completion_checkbox(context)


@when('Choose the wafer for creating AMG policy from the following options from the')
def step_impl(context):
    amgp.select_generate_assembly_map(context, "Pre PAT Final Probe (Probe Pass 1 OR M)")


@when('Choose the AMG format from "Conversion of Assembly Map File to Format" dropdown from the following list')
def step_impl(context):
    amgp.select_conversion_file_format(context, "ASCII TMA")


@when('Enter the "{main_dir}" folder path into the Input field')
def step_impl(context, main_dir):
    amgp.enter_folder_path(context, "D:\AMG")
    context.output_path = "D:\AMG"


@when('Enter the file name format into the input field, Enter @ in the input field options will be visible select any option from the list')
def step_impl(context):
    amgp.enter_file_name_format(context, "@FacilityID, @Date, @Time")


@when('Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)')
def step_impl(context):
    amgp.click_local_or_network_drive_radio_button(context)


@when('Check "Output Destination Of Assembly Map File" that path has been added')
def step_impl(context):
    amgp.verify_output_destination_amg_file_path(context, context.output_path)


@when('Saved policy is shown in the AMG Policies grid section')
def step_impl(context):
    amgp.verify_newly_created_amg_policy_name_on_grid(context, context.lot_completion_policy)


@when('Provide policy name as "{sbl_syl_integration_policy}" in "General" tab')
def step_impl(context, sbl_syl_integration_policy):
    context.sbl_syl_integration_policy_name = sbl_syl_integration_policy
    amgp.enter_into_assembly_policy_name_field(context, context.sbl_syl_integration_policy_name)


@when('Enable "Enable SBL/SYL Integration" checkbox')
def step_impl(context):
    amgp.check_sbl_syl_integration_checkbox(context)


@when('Saved SBL/SYL policy is shown in the AMG Policies grid section')
def step_impl(context):
    amgp.verify_newly_created_amg_policy_name_on_grid(context, context.sbl_syl_integration_policy_name)


@when('The AMG Policy will be successfully activated')
def step_impl(context):
    amgp.verify_automate_amg_policy_checkbox_is_enabled(context)


@when('A wafer will be saved into the desktop application and policy will also be saved into the "AssemblyMapPolicy" table in database')
def step_impl(context):
    pass


@when('File will also be saved into the given path')
def step_impl(context):
    pass


@when('Disable the check box that is available in front of each policy')
def step_impl(context):
    amgp.check_enable_policy_device_level_checkbox(context)


@when('Confirmation pop-up will appear with the written text message "Are you sure you want to un-automate this policy"')
def step_impl(context):
    amgp.accept_enable_policy_popup(context)


@when('Verify that when user clicks "YES", Page will be refreshed and popup stating "Policy status is updated successfully" will appear')
def step_impl(context):
    amgp.verify_success_popup_is_displayed(context)


@then('Verify that On the Assembly Map Policy window check box will be disabled and policy is un-automated')
def step_impl(context):
    amgp.verify_automate_amg_policy_checkbox_is_disabled(context)
    actions.logout(context)


@when('You will see the list of created AMG polices in "Assembly Map Policies" grid section')
def step_impl(context):
    amgp.verify_amg_policy_grid_is_displayed(context)


@when('Disable or Un-automate the policy that you want to update')
def step_impl(context):
    amgp.verify_automate_amg_policy_checkbox_is_disabled(context)


@when('Click the "Edit" icon against any policy that you want to update')
def step_impl(context):
    amgp.click_amg_policy_edit_button(context)


@when('Create assembly map policy window will open now you can make changes of your choice in the policy')
def step_impl(context):
    context.edited_policy_name_new_version = "AMG Policy Edited with New Version"
    amgp.edit_assembly_policy_name_field(context, context.edited_policy_name_new_version)


@when('Save changes pop-up will appear with message as "{pop_msg}"')
def step_impl(context, pop_msg):
    expected_text = pop_msg.strip()
    amgp.verify_save_changes_popup_text(context, expected_text)


@when('Check the "Save to a new version number option"')
def step_impl(context):
    amgp.check_new_version_radio_btn(context)


@when('Enter the new version like "{version_number}"')
def step_impl(context, version_number):
    amgp.enter_new_version_number(context, version_number)


@when('Click on OK button')
def step_impl(context):
    amgp.click_amg_policy_popup_ok_button(context)


@when('Confirmation pop-up will appear, a message written on the box is "{pop_msg}"')
def step_impl(context, pop_msg):
    expected_text = pop_msg.strip()
    amgp.verify_confirmation_popup_text(context, expected_text)


@when('Click on "Yes"')
def step_impl(context):
    amgp.click_confirmation_popup_yes_btn(context)


@when('"Successful automated policy has been saved" message will appear and page will be refresh')
def step_impl(context):
    amgp.verify_success_popup_is_displayed(context)


@then('Verify that a New entry of the updated policy with new version is added in the Assembly Map Policy grid section as an active policy')
def step_impl(context):
    amgp.verify_newly_created_amg_policy_name_on_grid(context, context.edited_policy_name_new_version)
    amgp.verify_newly_created_amg_policy_version_on_grid(context, "2.0")
    actions.logout(context)


@when('Create assembly map policy window will open now where you can make changes of your choice in the policy')
def step_impl(context):
    context.edited_policy_name_existing_version = "AMG Policy Edited with Existing Version"
    amgp.edit_assembly_policy_name_field(context, context.edited_policy_name_existing_version)


@when('Select "Keep Existing version number" option')
def step_impl(context):
    amgp.check_existing_version_radio_btn(context)


@then('Verify that a new entry of the updated policy with existing version is added in the Assembly Map Policy grid section as an active policy')
def step_impl(context):
    amgp.verify_newly_created_amg_policy_name_on_grid(context, context.edited_policy_name_existing_version)
    amgp.verify_newly_created_amg_policy_version_on_grid(context, "1.0")
    actions.logout(context)


@when('Click on the delete icon of AMG policy available at the end of each created policy')
def step_impl(context):
    amgp.click_amg_policy_delete_button(context)


@when('Create New Assembly Map Policy as a Pre-Requisite')
def step_impl(context):
    actions.create_new_amg_policy(context)


@when('"{delete_confirmation_msg}" popup appears')
def step_impl(context, delete_confirmation_msg):
    expected_text = delete_confirmation_msg.strip()
    amgp.verify_delete_confirmation_popup_text(context, expected_text)


@when('Number of wafers with status and count grid are shown on the confirmation popup window')
def step_impl(context):
    amgp.wafers_status_display(context)


@when('Click on the "Archive" button from the "Assembly Map Policy delete confirmation" popup')
def step_impl(context):
    amgp.click_archive_radio_btn(context)
    amgp.click_continue_btn(context)


@then('Verify that the Policy is Archived successfully')
def step_impl(context):
    amgp.verify_success_popup_is_displayed(context)
    actions.logout(context)


@when('Select the delete button')
def step_impl(context):
    amgp.click_delete_radio_btn(context)


@when('Click on continue button')
def step_impl(context):
    amgp.click_continue_btn(context)


@then('Verify that the AMG policy is deleted successfully')
def step_impl(context):
    amgp.verify_success_popup_is_displayed(context)
    actions.logout(context)


@when('Enable the checkbox "Turn on MES Integration"')
def step_impl(context):
    amgp.check_mes_Integration_checkbox(context)


@when('Choose the "G85 XML" format from "Conversion of Assembly Map File to Format"')
def step_impl(context):
    amgp.select_conversion_file_format(context, "G85 xml")


@when('After selecting AMG format from the above list Die bin details box will appear below in the "Generation" tab')
def step_impl(context):
    pass


@when('Add the path location of the standard rule file in the "File Directory" input field')
def step_impl(context):
    amgp.check_merge_assembly_map_checkbox(context)
    amgp.enter_file_dir_generations_tab(context, "D:\AMG")


@when('Add the file extension name without a dot on the input field of "File Extension"')
def step_impl(context):
    amgp.enter_file_ext_generations_tab(context, "csv")


@when('Choose the "SINF (3 Digit) 2" format from "Conversion of Assembly Map File to Format"')
def step_impl(context):
    amgp.select_conversion_file_format(context, "SINF (3 Digit) 2")


@when('After selecting AMG format from the above list Die bin details box will appear below the "Generation" tab')
def step_impl(context):
    pass


@when('Enable "Die Type" and select die type from the drop-down list')
def step_impl(context):
    amgp.check_die_type_checkbox(context)
    amgp.select_die_type__dropdown_value(context, "Probe Die(s)")


@when('Enable "Bin definition" and add Hard Bin/Soft Bin number in the input field')
def step_impl(context):
    amgp.check_bin_definition_checkbox(context)
    amgp.enter_hard_bin(context, "74")


@when('Enable "Pass/Fail Bin Flag" and select the pass/fail flag from the drop-down list')
def step_impl(context):
    amgp.pass_fail_bin_flag_checkbox(context)
    amgp.select_bin_flag_dropdown_value(context, "Pass Bin")


@when('Enter Die Character in the input field user can add a maximum of 3 characters')
def step_impl(context):
    amgp.enter_die_characters(context, "123")


@when('After selecting/adding complete die bin details click on the "Add Die/Bin Detail" button')
def step_impl(context):
    amgp.click_add_die_bin_details_btn(context)


@when('All the Die/Bin details will be added in the "Saved Die/Bin Details" section')
def step_impl(context):
    amgp.verify_saved_die_type_xpath(context, "Probe Die(s)")


@when('Enable "Merge Assembly Map with Device Map"')
def step_impl(context):
    pass


@when('Make sure that standard rule file name and device name are same')
def step_impl(context):
    pass


@when('Enable the "Apply AMG Policy To Device Level" check box')
def step_impl(context):
    amgp.check_apply_amg_policy_to_device_level_checkbox(context)
    amgp.test_program_is_disabled(context)

