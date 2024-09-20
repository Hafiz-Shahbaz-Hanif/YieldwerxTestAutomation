import time

from Pages.AMGMapGenerationsPage import AMGMapGenerationsClass
from Pages.DashboardPage import DashboardClass
from Pages.LoginPage import LoginClass
from Pages.NewAMGPolicyWindowPage import NewAMGPolicyClass
from utilities.customLogger import LogGen

logger = LogGen.loggen()
lg = LoginClass()
dc = DashboardClass()
amgp = NewAMGPolicyClass()
amg_gen = AMGMapGenerationsClass()


class ActionsClass:
    def __init__(self):
        pass

    def login(self, context):
        lg.launchBrowser(context)
        lg.openWebsite(context)
        lg.verifyLoginPageOpened(context)
        lg.enterUsernamePassword(context)
        lg.hitLoginButton(context)
        lg.verifyDashboard(context)

    def logout(self, context):
        time.sleep(5)
        dc.click_on_logout_avatar(context)
        dc.click_on_logout_link(context)
        lg.verifyLoginPageOpened(context)
        lg.quiteBrowser(context)

    def create_new_amg_policy(self, context):
        amgp.click_create_assembly_map_policy_button(context)
        context.policy_name = "Device Level Policy"
        amgp.enter_into_assembly_policy_name_field(context, context.policy_name)
        amgp.navigate_to_parameters_tab(context)
        amgp.click_facility(context)
        amgp.check_apply_amg_policy_to_device_level_checkbox(context)
        amgp.test_program_is_disabled(context)
        amgp.check_sbl_syl_integration_checkbox(context)
        amgp.select_generate_assembly_map(context, "Pre PAT Final Probe (Probe Pass 1 OR M)")
        amgp.navigate_to_generation_tab(context)
        amgp.select_conversion_file_format(context, "ASCII TMA")
        amgp.navigate_to_output_tab(context)
        amgp.enter_folder_path(context, "D:\AMG")
        context.output_path = "D:\AMG"
        amgp.click_amg_map_file_exists_radio_button(context)
        amgp.enter_file_name_format(context, "@FacilityID, @Date, @Time")
        amgp.click_local_or_network_drive_radio_button(context)
        amgp.click_add_path_button(context)
        amgp.verify_output_destination_amg_file_path(context, context.output_path)
        amgp.check_save_assembly_map_checkbox(context)
        amgp.click_amg_policy_save_button(context)
        amgp.verify_newly_created_amg_policy_name_on_grid(context, context.policy_name)

    def create_new_amg_test_program_level_policy(self, context):
        amgp.click_create_assembly_map_policy_button(context)
        context.policy_name = "Test Program Level Policy"
        amgp.enter_into_assembly_policy_name_field(context, context.policy_name)
        amgp.navigate_to_parameters_tab(context)
        amgp.click_facility(context)
        amgp.click_test_program(context)
        amgp.select_generate_assembly_map(context, "Pre PAT Final Probe (Probe Pass 1 OR M)")
        amgp.navigate_to_generation_tab(context)
        amgp.select_conversion_file_format(context, "ASCII TMA")
        amgp.navigate_to_output_tab(context)
        amgp.enter_folder_path(context, "D:\AMG")
        context.output_path = "D:\AMG"
        amgp.click_amg_map_file_exists_radio_button(context)
        amgp.enter_file_name_format(context, "@FacilityID, @Date, @Time")
        amgp.click_local_or_network_drive_radio_button(context)
        amgp.click_add_path_button(context)
        amgp.verify_output_destination_amg_file_path(context, context.output_path)
        amgp.check_save_assembly_map_checkbox(context)
        amgp.click_amg_policy_save_button(context)
        amgp.verify_newly_created_amg_policy_name_on_grid(context, context.policy_name)

    def verify_amg_policy_display_on_generations_tab(self, context):
        amg_gen.verify_amg_policy_display_on_generations_tab(context, context.policy_name)

    def delete_created_amg_policy(self, context):
        time.sleep(3)
        dc.click_assembly_map_policies_heading(context)
        amgp.verify_amg_policy_grid_is_displayed(context)
        amgp.click_amg_policy_delete_button(context)
        popup_text = "Assembly Map Policy delete confirmation"
        expected_text = popup_text.strip()
        amgp.verify_delete_confirmation_popup_text(context, expected_text)
        amgp.wafers_status_display(context)
        amgp.click_delete_radio_btn(context)
        amgp.click_continue_btn(context)


