import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AMGManualAssemblyClass:

    def __init__(self):
        pass

    loader = "(//body[@class='loading'])[1]"
    lot_id = "cb_LotsGrid"
    reset_btn_id = "btn-reset"
    wafer_plotting_dropdown_id = "WaferPlottingType"
    plot_wafer_Map_btn_xpath = "//input[@value='Plot Wafer Map to Pick Die(s)']"
    facility_xpath = "//option[@value='SILICON']"
    silicon_lot_id = "jqg_LotsGrid_72"
    wafer_container_id = "AMGWafer_container"
    wafer_die_css = "path[fill='#008000'][d='M 278.57142857142856 120.5 L 298.6103896103896 120.5 298.6103896103896 132.83333333333334 278.57142857142856 132.83333333333334 Z']"
    calculated_wafer_die_css = "path[fill='#008000'][d='M 327.27272727272725 144.5 L 339.9090909090909 144.5 339.9090909090909 167.5 327.27272727272725 167.5 Z']"
    plus_sign_xpath = "//span[normalize-space()='+']"
    mark_as_assemble_option_xpath = "//button[@onclick='dieAssembledClick()']//span//img"
    success_popup_css = "div.bootstrap-growl.alert.alert-success"
    save_generate_amg_option_xpath = "//button[@onclick='amgSaveAndGenerateClick()']//span//img"
    generations_tab_id = "generation-tab"
    save_generate_assembly_map_btn_xpath = "//input[@value='Save and Generate Assembly Map']"
    probe_count_xpath = "//td[@title='MA1']"
    conversion_file_format_dropdown_id = "ConversionFileFormatID"
    saved_pick_map_die_type_xpath = "//table[@id='AssemblyMapDieTypeSymbol_Grid']/tbody/tr[2]/td[8]"
    pick_map_file_name_format_field_id = "FileNameFormat"
    pick_map_output_destination_amg_file_xpath = "//table[@id='PickMapPathGrid']/tbody/tr[2]/td[9]"
    amg_pick_map_manual_assembly_heading_xpath = "(//span[normalize-space()='Generate Manual Assembly / Pick Map'])[1]"
    web_small_dataset_facility_xpath = "//option[@value='WEB SMALL DATASET']"
    wafer_id_checkbox_xpath = "//table[@id='WafersGrid']/tbody/tr[2]/td[1]/input"
    sftp_radio_btn_id = "rdbtnSftp"
    sftp_uname_id = "FTPUname"
    sftp_pwd_id = "FTPPwd"
    sftp_file_name_format = "FileNameFormat"

    def click_pick_map_manual_assembly_map_heading(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.amg_pick_map_manual_assembly_heading_xpath).click()

    def verify_pick_map_output_destination_amg_file_path(self, context, expected_text):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.pick_map_output_destination_amg_file_xpath)
        assert element.text.__eq__(expected_text)

    def verify_pick_map_saved_die_type_xpath(self, context, expected_text):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.saved_pick_map_die_type_xpath)
        assert element.text.__eq__(expected_text)

    def enter_pick_map_file_name_format(self, context, format_value):
        context.driver.find_element(By.ID, self.pick_map_file_name_format_field_id).send_keys(format_value)

    def verify_success_popup_is_displayed(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.success_popup_css)))
        assert element

    def verify_lot_id_checkbox_is_checked(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.ID, self.lot_id)
        assert element.is_selected()

    def verify_silicon_lot_id_is_checked(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.ID, self.silicon_lot_id)
        assert element.is_selected()

    def verify_lot_id_checkbox_is_unchecked(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.ID, self.lot_id)
        assert element.is_selected() is False

    def verify_wafer_container_is_displayed(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        wait2 = WebDriverWait(context.driver, 60)
        element = wait2.until(EC.visibility_of_element_located((By.ID, self.wafer_container_id)))
        assert element.is_displayed()

    def verify_generations_tab_is_displayed(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.ID, self.generations_tab_id)
        assert element.is_displayed()

    def verify_MA1_probe_is_displayed(self, context):
        time.sleep(5)
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.probe_count_xpath)))
        assert element

    def click_reset_btn(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.reset_btn_id).click()

    def click_wafer_die(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        time.sleep(5)
        context.driver.find_element(By.CSS_SELECTOR, self.wafer_die_css).click()

    def click_calculated_wafer_die_css(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        time.sleep(5)
        context.driver.find_element(By.CSS_SELECTOR, self.calculated_wafer_die_css).click()

    def click_plus_sign(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.plus_sign_xpath).click()

    def click_plot_wafer_Map_btn(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.plot_wafer_Map_btn_xpath).click()

    def click_facility(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.facility_xpath))).click()

    def click_web_small_dataset_facility(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.web_small_dataset_facility_xpath))).click()

    def verify_wafer_id_is_selected(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        time.sleep(5)
        element = context.driver.find_element(By.XPATH, self.wafer_id_checkbox_xpath)
        assert element.is_selected

    def click_mark_as_assemble_option(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.mark_as_assemble_option_xpath))).click()

    def click_save_generate_amg_option(self, context):
        context.driver.find_element(By.XPATH, self.save_generate_amg_option_xpath).click()

    def click_save_generate_assembly_map_btn(self, context):
        context.driver.find_element(By.XPATH, self.save_generate_assembly_map_btn_xpath).click()

    def select_wafer_plotting_option(self, context, visible_text_value):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = Select(context.driver.find_element(By.ID, self.wafer_plotting_dropdown_id))
        element.select_by_visible_text(visible_text_value)

    def select_conversion_file_format_for_pick_map(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.ID, self.conversion_file_format_dropdown_id))
        element.select_by_visible_text(visible_text_value)

    def click_SFTP_drive_radio_button(self, context):
        context.driver.find_element(By.ID, self.sftp_radio_btn_id).click()

    def enter_SFTP_user_and_pass(self, context, username, password):
        context.driver.find_element(By.ID, self.sftp_uname_id).send_keys(username)
        context.driver.find_element(By.ID, self.sftp_pwd_id).send_keys(password)

    def enter_SFTP_file_name_format(self, context, file_name):
        context.driver.find_element(By.ID, self.sftp_file_name_format).send_keys(file_name)









