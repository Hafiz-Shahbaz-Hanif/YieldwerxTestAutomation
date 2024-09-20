import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class NewAMGPolicyClass:

    def __init__(self):
        pass

    i = 1
    loader = "(//body[@class='loading'])[1]"
    create_assembly_map_policy_xpath = "//span[normalize-space()='Create Assembly Map Policy']"
    assembly_policy_name_id = "Assembly_Policy_Name"
    parameters_tab_id = "parameter-tab"
    generations_tab_id = "generation-tab"
    output_tab_id = "output-tab"
    facility_xpath = "//option[@value='WEB SMALL DATASET']"
    generate_assembly_map_from_id = "GenerateAssemblyMapFrom"
    conversion_file_format_dropdown_id = "Conversion_FileFormat"
    main_dir_field_id = "LocalDirectory_Location"
    amg_file_exists_radio_btn_id = "rdbtnrename"
    file_name_format_field_id = "selectFileName"
    local_or_network_drive_id = "rdbtnLocal"
    add_path_btn_id = "add-path"
    output_destination_amg_file_xpath = "//table[@id='AssemblyMapDestinationPaths']/tbody/tr[2]/td[9]"
    newly_created_amg_policy_name_grid_xpath = "//table[@id='AssemblyMapsGrid']/tbody/tr[2]/td[5]"
    newly_created_amg_policy_version_grid_xpath = "//table[@id='AssemblyMapsGrid']/tbody/tr[2]/td[6]"
    save_assembly_map_checkbox_id = "IsSaveWafer"
    amg_policy_save_btn_id = "btn-save"
    enable_policy_checkbox_xpath = "//table[@id='AssemblyMapsGrid']/tbody/tr[2]/td[1]/input"
    automate_amg_policy_popup_yes_btn_xpath = "//button[normalize-space()='Yes']"
    apply_amg_policy_to_device_level_checkbox_id = "IsPATPolicyApplied_ToDevice"
    enable_policy_device_level_checkbox_xpath = "//table[@id='AssemblyMapsGrid']/tbody/tr[2]/td[1]/input"
    lot_completion_checkbox_id = "IsLot_Completed"
    test_program_section_id = "Test_Program"
    sbl_syl_integration_checkbox_id = "Is_Sbyl_Required"
    swm_delete_success_popup_css = "div.bootstrap-growl.alert.alert-success"
    amg_grid_id = "AssemblyMapsGrid"
    amg_policy_edit_btn_xpath = "//table[@id='AssemblyMapsGrid']/tbody/tr[2]/td[4]/button/span"
    amg_policy_delete_btn_xpath = "//table[@id='AssemblyMapsGrid']/tbody/tr[2]/td[19]/button/span"
    save_changes_popup_text_xpath = "//div[@id='modal-text']/p"
    delete_confirmation_popup_text_xpath = "#modal-form-label"
    new_version_radio_btn_xpath = "//input[@value='NewVersion']"
    existing_version_radio_btn_xpath = "//input[@value='ExistingVersion']"
    new_version_txt_id = "new-version-txt"
    ok_btn_id = "btn-ok"
    confirmation_popup_text_css = "div.modal-body.warning-dialog-body p"
    confirmation_popup_yes_btn_id = "cancel-edit-dialog"
    wafers_status_id = "GetStatusesGrid"
    archive_radio_btn_id = "radio-btn-archive"
    delete_radio_btn_id = "radio-btn-soft-delete"
    continue_btn_id = "btn-yes"
    mes_integration_checkbox_id = "MES_Integration"
    merge_assembly_map_checkbox_id = "Isstaticassemblymap"
    enter_file_dir_on_generations_tab_id = "StaticFileDirPath"
    enter_file_ext_on_generations_tab_id = "StaticFileExtension"
    select_die_type_checkbox_id = "isSelectDieType"
    select_die_type_dropdown_id = "symbolDieTypes"
    bin_definition_checkbox_id = "isDefineBinNumbers"
    hard_bin_field_id = "hardBinNumber"
    pass_fail_bin_flag_checkbox_id = "isPassFailBinFlag"
    select_bin_flag_dropdown_id = "passFailBinFlag"
    die_character_field_id = "symbol"
    add_die_bin_details_btn_id = "addSymbol"
    saved_die_type_xpath = "//table[@id='AssemblyMapDieTypeSymbolDefinition']/tbody/tr[2]/td[8]"
    test_program_xpath = "//option[@value='PREBAKE_A_4670']"

    def verify_success_popup_is_displayed(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.swm_delete_success_popup_css)))
        context.driver.find_element(By.CSS_SELECTOR, self.swm_delete_success_popup_css).is_displayed()

    def verify_saved_die_type_xpath(self, context, expected_text):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.saved_die_type_xpath)
        assert element.text.__eq__(expected_text)

    def click_create_assembly_map_policy_button(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.create_assembly_map_policy_xpath).click()

    def enter_new_version_number(self, context, name_value):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.new_version_txt_id).send_keys(name_value)

    def enter_into_assembly_policy_name_field(self, context, name_value):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.assembly_policy_name_id).send_keys(name_value)

    def edit_assembly_policy_name_field(self, context, name_value):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.ID, self.assembly_policy_name_id)
        element.clear()
        element.send_keys(name_value)

    def enter_folder_path(self, context, path_value):
        context.driver.find_element(By.ID, self.main_dir_field_id).send_keys(path_value)

    def enter_file_dir_generations_tab(self, context, path_value):
        context.driver.find_element(By.ID, self.enter_file_dir_on_generations_tab_id).send_keys(path_value)

    def enter_file_ext_generations_tab(self, context, path_value):
        context.driver.find_element(By.ID, self.enter_file_ext_on_generations_tab_id).send_keys(path_value)

    def enter_file_name_format(self, context, format_value):
        context.driver.find_element(By.ID, self.file_name_format_field_id).send_keys(format_value)

    def enter_hard_bin(self, context, format_value):
        context.driver.find_element(By.ID, self.hard_bin_field_id).send_keys(format_value)

    def enter_die_characters(self, context, format_value):
        context.driver.find_element(By.ID, self.die_character_field_id).send_keys(format_value)

    def navigate_to_parameters_tab(self, context):
        context.driver.find_element(By.ID, self.parameters_tab_id).click()

    def navigate_to_generation_tab(self, context):
        context.driver.find_element(By.ID, self.generations_tab_id).click()

    def navigate_to_output_tab(self, context):
        context.driver.find_element(By.ID, self.output_tab_id).click()

    def click_facility(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.facility_xpath))).click()

    def click_test_program(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.test_program_xpath))).click()

    def click_amg_map_file_exists_radio_button(self, context):
        context.driver.find_element(By.ID, self.amg_file_exists_radio_btn_id).click()

    def click_local_or_network_drive_radio_button(self, context):
        context.driver.find_element(By.ID, self.local_or_network_drive_id).click()

    def click_add_path_button(self, context):
        context.driver.find_element(By.ID, self.add_path_btn_id).click()

    def click_add_die_bin_details_btn(self, context):
        context.driver.find_element(By.ID, self.add_die_bin_details_btn_id).click()

    def click_amg_policy_save_button(self, context):
        context.driver.find_element(By.ID, self.amg_policy_save_btn_id).click()

    def click_amg_policy_edit_button(self, context):
        context.driver.find_element(By.XPATH, self.amg_policy_edit_btn_xpath).click()

    def click_amg_policy_delete_button(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.amg_policy_delete_btn_xpath).click()

    def click_amg_policy_popup_ok_button(self, context):
        context.driver.find_element(By.ID, self.ok_btn_id).click()

    def click_confirmation_popup_yes_btn(self, context):
        context.driver.find_element(By.ID, self.confirmation_popup_yes_btn_id).click()

    def click_archive_radio_btn(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.archive_radio_btn_id).click()

    def click_delete_radio_btn(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.delete_radio_btn_id).click()

    def click_continue_btn(self, context):
        context.driver.find_element(By.ID, self.continue_btn_id).click()

    def select_generate_assembly_map(self, context, visible_text_value):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = Select(context.driver.find_element(By.ID, self.generate_assembly_map_from_id))
        element.select_by_visible_text(visible_text_value)

    def select_conversion_file_format(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.ID, self.conversion_file_format_dropdown_id))
        element.select_by_visible_text(visible_text_value)

    def select_die_type__dropdown_value(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.ID, self.select_die_type_dropdown_id))
        element.select_by_visible_text(visible_text_value)

    def select_bin_flag_dropdown_value(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.ID, self.select_bin_flag_dropdown_id))
        element.select_by_visible_text(visible_text_value)

    def verify_output_destination_amg_file_path(self, context, expected_text):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.output_destination_amg_file_xpath)
        assert element.text.__eq__(expected_text)

    def verify_newly_created_amg_policy_name_on_grid(self, context, expected_text):
        time.sleep(5)
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.newly_created_amg_policy_name_grid_xpath)))
        element = context.driver.find_element(By.XPATH, self.newly_created_amg_policy_name_grid_xpath)
        assert element.text.__eq__(expected_text)

    def verify_newly_created_amg_policy_version_on_grid(self, context, expected_text):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.newly_created_amg_policy_version_grid_xpath)))
        element = context.driver.find_element(By.XPATH, self.newly_created_amg_policy_version_grid_xpath)
        assert element.text.__eq__(expected_text)

    def verify_amg_policy_grid_is_displayed(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.amg_grid_id).is_displayed()

    def check_save_assembly_map_checkbox(self, context):
        context.driver.find_element(By.ID, self.save_assembly_map_checkbox_id).click()

    def check_enable_policy_checkbox(self, context):
        context.driver.find_element(By.XPATH, self.enable_policy_checkbox_xpath).click()

    def check_enable_policy_device_level_checkbox(self, context):
        context.driver.find_element(By.XPATH, self.enable_policy_checkbox_xpath).click()

    def check_apply_amg_policy_to_device_level_checkbox(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.apply_amg_policy_to_device_level_checkbox_id).click()

    def check_for_lot_completion_checkbox(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.lot_completion_checkbox_id).click()

    def check_sbl_syl_integration_checkbox(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.sbl_syl_integration_checkbox_id).click()

    def check_mes_Integration_checkbox(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.mes_integration_checkbox_id).click()

    def check_merge_assembly_map_checkbox(self, context):
        context.driver.find_element(By.ID, self.merge_assembly_map_checkbox_id).click()

    def check_new_version_radio_btn(self, context):
        context.driver.find_element(By.XPATH, self.new_version_radio_btn_xpath).click()

    def check_existing_version_radio_btn(self, context):
        context.driver.find_element(By.XPATH, self.existing_version_radio_btn_xpath).click()

    def check_die_type_checkbox(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.select_die_type_checkbox_id).click()

    def check_bin_definition_checkbox(self, context):
        context.driver.find_element(By.ID, self.bin_definition_checkbox_id).click()

    def pass_fail_bin_flag_checkbox(self, context):
        context.driver.find_element(By.ID, self.pass_fail_bin_flag_checkbox_id).click()

    def test_program_is_disabled(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.ID, self.test_program_section_id)
        assert element.is_enabled() is False

    def accept_enable_policy_popup(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.automate_amg_policy_popup_yes_btn_xpath).click()

    def verify_automate_amg_policy_checkbox_is_enabled(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.enable_policy_checkbox_xpath)
        assert element.is_selected()

    def verify_automate_amg_policy_checkbox_is_disabled(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.enable_policy_checkbox_xpath)
        assert element.is_selected() is False

    def verify_save_changes_popup_text(self, context, expected_text):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.save_changes_popup_text_xpath)))
        element = context.driver.find_element(By.XPATH, self.save_changes_popup_text_xpath)
        actual_text = element.text.strip()
        assert actual_text.__eq__(expected_text)

    def verify_delete_confirmation_popup_text(self, context, expected_text):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.delete_confirmation_popup_text_xpath)))
        element = context.driver.find_element(By.CSS_SELECTOR, self.delete_confirmation_popup_text_xpath)
        actual_text = element.text.strip()
        assert actual_text.__eq__(expected_text)

    def verify_confirmation_popup_text(self, context, expected_text):
        time.sleep(5)
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.confirmation_popup_text_css)))
        element = context.driver.find_element(By.CSS_SELECTOR, self.confirmation_popup_text_css)
        actual_text = element.text.strip()
        assert actual_text.__eq__(expected_text)

    def wafers_status_display(self, context):
        element = context.driver.find_element(By.ID, self.wafers_status_id)
        assert element.is_displayed()


