import time

from behave import *
from Pages.AMGPickMapPage import AMGManualAssemblyClass
from Pages.ActionsPage import ActionsClass
from Pages.DashboardPage import DashboardClass
from Pages.NewAMGPolicyWindowPage import NewAMGPolicyClass

actions = ActionsClass()
dc = DashboardClass()
amgp = NewAMGPolicyClass()
amg_manual = AMGManualAssemblyClass()


@when('Open Generate Manual Assembly/Pick Map')
def step_impl(context):
    dc.click_assembly_map_heading(context)
    dc.click_manual_assembly_map_heading(context)


@when('Select facility data to generate Manual Assembly/Pick Map')
def step_impl(context):
    amgp.click_facility(context)


@when('After selecting the data facility, Work Center, Device, Test Program, Lot, and wafers should be selected automatically')
def step_impl(context):
    amg_manual.verify_lot_id_checkbox_is_checked(context)


@when('Click on the Reset Button')
def step_impl(context):
    amg_manual.click_reset_btn(context)


@then('Verify that All the data selections are reset')
def step_impl(context):
    amg_manual.verify_lot_id_checkbox_is_unchecked(context)
    actions.logout(context)


@when('Select the facility data')
def step_impl(context):
    amg_manual.click_facility(context)


@when('After selecting the facility, work center, device, test program, lot and wafer will be selected automatically')
def step_impl(context):
    amg_manual.verify_silicon_lot_id_is_checked(context)


@when('Select the Wafer plotting option as "{wafer_plotting_option}"')
def step_impl(context, wafer_plotting_option):
    amg_manual.select_wafer_plotting_option(context, wafer_plotting_option)


@when('Click on the Plot Wafer Map to Pick Map Die(S)')
def step_impl(context):
    amg_manual.click_plot_wafer_Map_btn(context)


@when('User will be redirected to the Bin Wafer Map screen')
def step_impl(context):
    amg_manual.verify_wafer_container_is_displayed(context)


@when('Select the few wafers die')
def step_impl(context):
    amg_manual.click_wafer_die(context)


@when('Click on the plus sign available at the end on right side and expand the options')
def step_impl(context):
    amg_manual.click_plus_sign(context)


@when('Select mark as assemble from the option')
def step_impl(context):
    amg_manual.click_mark_as_assemble_option(context)


@when('"Selected dies have been marked as assembled" message will appear and selected dies will be marked')
def step_impl(context):
    # amg_manual.verify_success_popup_is_displayed(context)
    pass


@when('Again click on the plus sign available at the end on the right side and expand the options')
def step_impl(context):
    amg_manual.click_plus_sign(context)


@when('Click on the "Save and generate AMG"')
def step_impl(context):
    amg_manual.click_save_generate_amg_option(context)


@when('User will be redirected to "Generations" tab')
def step_impl(context):
    amg_manual.verify_generations_tab_is_displayed(context)


@when('Choose the "ASCII TXT" format from "Conversion of Assembly Map File to Format"')
def step_impl(context):
    amg_manual.select_conversion_file_format_for_pick_map(context, "ASCII TXT")


@when('Enter Die Character in the input field user can add a maximum of 2 characters')
def step_impl(context):
    amgp.enter_die_characters(context, "12")


@when('Click on the "Save and generate Assembly Map" button')
def step_impl(context):
    amg_manual.click_save_generate_assembly_map_btn(context)


@when('All the details of Die/Bin will be added in the "Saved Die/Bin Details" section')
def step_impl(context):
    amg_manual.verify_pick_map_saved_die_type_xpath(context, "Probe Die(s)")


@when('Enter file name format in input field, Enter @ in the input field options will be visible select any option from the list')
def step_impl(context):
    amg_manual.enter_pick_map_file_name_format(context, "@FacilityID, @Date, @Time")


@when('Enter "{main_dir}" folder path in Input field')
def step_impl(context, main_dir):
    amgp.enter_folder_path(context, "D:\AMG")
    context.output_path = "D:\AMG"


@when('Check the "Output Destination Of Assembly Map File" to make sure that path has been added')
def step_impl(context):
    amg_manual.verify_pick_map_output_destination_amg_file_path(context, context.output_path)


@then('Verify that a new assembly map wafer was saved into the database with MA1 wafer')
def step_impl(context):
    amg_manual.click_pick_map_manual_assembly_map_heading(context)
    amg_manual.click_facility(context)
    amg_manual.verify_MA1_probe_is_displayed(context)
    actions.logout(context)


@when('After selecting facility, work center, device, test program, lot and wafer will be selected automatically')
def step_impl(context):
    pass


@when('Select the data set size as "{data_set_size}" and facility as "{facility}"')
def step_impl(context, data_set_size, facility):
    amg_manual.click_web_small_dataset_facility(context)


@when('Select the "{wafer_id}" from wafers')
def step_impl(context, wafer_id):
    amg_manual.verify_wafer_id_is_selected(context)


@when('Select Wafer plotting option as "{wafer_plotting_option}"')
def step_impl(context, wafer_plotting_option):
    amg_manual.select_wafer_plotting_option(context, wafer_plotting_option)


@when('Choose the "{file_format}" format')
def step_impl(context, file_format):
    amg_manual.select_conversion_file_format_for_pick_map(context, file_format)


@when('Select the few wafer dies (as seen in the attached images)')
def step_impl(context):
    amg_manual.click_calculated_wafer_die_css(context)


@when('Enter the "{main_dir}" folder path in Input field')
def step_impl(context, main_dir):
    amgp.enter_folder_path(context, main_dir)
    context.output_path_for_calculated_wafer = main_dir


@when('Check "Output Destination Of Assembly Map File" to make sure that path has been added')
def step_impl(context):
    amg_manual.verify_pick_map_output_destination_amg_file_path(context, context.output_path_for_calculated_wafer)


@then('Verify that the new assembly map wafer was saved into the database with MA1 wafer')
def step_impl(context):
    amg_manual.click_pick_map_manual_assembly_map_heading(context)
    amg_manual.click_web_small_dataset_facility(context)
    amg_manual.verify_MA1_probe_is_displayed(context)
    actions.logout(context)


@when('Choose the AMG format from "Conversion of Assembly Map File to Format"')
def step_impl(context):
    amg_manual.select_conversion_file_format_for_pick_map(context, "ASCII TMA")


@when('Choose the output path as (FTP Drive/SFTP Drive)')
def step_impl(context):
    amg_manual.click_SFTP_drive_radio_button(context)


@when('Enter the user name as "{username}" and password as "{password}" for FTP/SFTP drive')
def step_impl(context, username, password):
    amg_manual.enter_SFTP_user_and_pass(context, username, password)
    amgp.click_amg_map_file_exists_radio_button(context)


@when('Enter the path of FTP/SFTP Drive into the main directory input field')
def step_impl(context):
    amgp.enter_folder_path(context, "sftp://192.168.0.18/22")
    context.output_sftp_path = "sftp://192.168.0.18/22"


@when('Check on the "Output Destination Of Assembly Map File" that the path has been added')
def step_impl(context):
    amg_manual.verify_pick_map_output_destination_amg_file_path(context, context.output_sftp_path)


@when('Enter the file name format into the input field, Enter @ in the input field options will be visible select any option from the list for SFTP option')
def step_impl(context):
    amg_manual.enter_SFTP_file_name_format(context, "@FacilityID, @Date, @Time")




