import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class NewSWMManualClass:

    def __init__(self):
        pass

    loader = "(//body[@class='loading'])[1]"
    swm_manual_source_facility_xpath = "(//option[@value='WEB SMALL DATASET'][normalize-space()='WEB SMALL DATASET'])[1]"
    swm_manual_source_workcenter_xpath = "(//option[@value='WAFER SORT'])[1]"
    swm_manual_source_device_xpath = "(//option[@value='4670'])[1]"
    swm_manual_source_testprogram_xpath = "(//option[@value='PREBAKE_A_4670'])[1]"
    swm_manual_target_facility_xpath = "(//option[@value='WEB SMALL DATASET'][normalize-space()='WEB SMALL DATASET'])[2]"
    swm_manual_target_workcenter_xpath = "(//option[@value='WAFER SORT'][normalize-space()='WAFER SORT'])[2]"
    swm_manual_target_device_xpath = "(//option[@value='4670'][normalize-space()='4670'])[2]"
    swm_manual_target_testprogram_xpath = "(//option[@value='POSTBAKE_A_4670'])[1]"
    swm_manual_target_testprogram_devicelevel_xpath = "(//option[@value='POSTBAKE_A_4670'])[2]"
    swm_manual_wafer_plotting_dropdown_xpath = "(//select[@id='WaferPlottingType'])[1]"
    swm_manual_generate_button_xpath = "//input[@id='btn-calculate']"
    swm_source_wafer_map_xpath = "//div[@id='SourceWafer_container']"
    swm_target_wafer_map_xpath = "//div[@id='TargetWafer_container']"
    swm_combine_wafer_map_xpath = "//div[@id='CombineWafer_container']"
    swm_manual_edit_policy_button_xpath = "//button[@id='cmd-execute']"
    swm_manual_edit_policy_output_data_selection_tab_xpath = "//a[@id='output-data-selection-tab']"
    swm_manual_edit_policy_metadata_selection_form_xpath = "//select[@id='MetaDataID']"
    swm_manual_unselect_all_source_die_button_xpath = "//button[@onclick='unselectSourceAllDieTypeFilters()']"
    swm_manual_unselect_all_target_die_button_xpath = "//button[@onclick='unselectTargetAllDieTypeFilters()']"
    swm_manual_edit_policy_save_btn_xpath = "//input[@id='btn-save-policy']"
    swm_manual_policy_changes_ok_btn_xpath = "//button[@id='btn-ok']"

    def click_swm_manual_source_facility(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.swm_manual_source_facility_xpath).click()

    def click_swm_manual_source_workcenter(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.swm_manual_source_workcenter_xpath).click()

    def click_swm_manual_source_device(self, context):
        context.driver.find_element(By.XPATH, self.swm_manual_source_device_xpath).click()

    def click_swm_manual_source_testprogram(self, context):
        context.driver.find_element(By.XPATH, self.swm_manual_source_testprogram_xpath).click()

    def click_swm_manual_target_facility(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.swm_manual_target_facility_xpath).click()

    def click_swm_manual_target_workcenter(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.swm_manual_target_workcenter_xpath).click()

    def click_swm_manual_target_device(self, context):
        context.driver.find_element(By.XPATH, self.swm_manual_target_device_xpath).click()

    def click_swm_manual_target_testprogram(self, context):
        context.driver.find_element(By.XPATH, self.swm_manual_target_testprogram_xpath).click()

    def click_swm_manual_target_testprogram_device_level(self, context):
        context.driver.find_element(By.XPATH, self.swm_manual_target_testprogram_devicelevel_xpath).click()

    def click_swm_manual_edit_policy_button(self, context):
        context.driver.find_element(By.XPATH, self.swm_manual_edit_policy_button_xpath).click()

    def click_swm_manual_unselect_source_button(self, context):
        context.driver.find_element(By.XPATH, self.swm_manual_unselect_all_source_die_button_xpath).click()

    def click_swm_manual_unselect_target_button(self, context):
        context.driver.find_element(By.XPATH, self.swm_manual_unselect_all_target_die_button_xpath).click()

    def click_swm_manual_edit_policy_save_btn(self, context):
        context.driver.find_element(By.XPATH, self.swm_manual_edit_policy_save_btn_xpath).click()

    def click_swm_manual_generate_button(self, context):
        time.sleep(3)
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        context.driver.find_element(By.XPATH, self.swm_manual_generate_button_xpath).click()

    def click_swm_manual_edit_policy_output_data_selection_tab(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.swm_manual_edit_policy_output_data_selection_tab_xpath).click()

    def click_swm_manual_policy_ok_btn(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        time.sleep(2)
        context.driver.find_element(By.XPATH, self.swm_manual_policy_changes_ok_btn_xpath).click()

    def select_wafer_plotting_option(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.XPATH, self.swm_manual_wafer_plotting_dropdown_xpath))
        element.select_by_visible_text(visible_text_value)

    def select_swm_manual_edit_policy_metadata_selection_form(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.XPATH, self.swm_manual_edit_policy_metadata_selection_form_xpath))
        element.select_by_visible_text(visible_text_value)

    def verify_wafer_map_is_displayed(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.swm_source_wafer_map_xpath).is_displayed()
        context.driver.find_element(By.XPATH, self.swm_target_wafer_map_xpath).is_displayed()
        context.driver.find_element(By.XPATH, self.swm_combine_wafer_map_xpath).is_displayed()



