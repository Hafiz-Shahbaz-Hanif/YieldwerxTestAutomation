import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class ManualAMGPolicyExecution:

    def __init__(self):
        pass

    loader = "(//body[@class='loading'])[1]"
    lod_id_checkbox_xpath = "//table[@id='LotsGrid']/tbody/tr[2]/td[1]/input"
    wafer_checkbox_xpath = "//table[@id='WafersGrid']/tbody/tr[2]/td[1]/input"
    work_center_xpath = "//option[@value='WAFER SORT']"
    test_program_level_policy_xpath = "//table[@id='PoliciesGrid']/tbody/tr[2]/td[2]"
    device_level_policy_xpath = "//table[@id='PoliciesGrid']/tbody/tr[3]/td[2]"
    policy_based_map_btn_id = "btn-process-wafers"
    success_popup_css = "div.bootstrap-growl.alert.alert-success"

    def verify_success_popup_is_displayed(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.success_popup_css)))
        element = context.driver.find_element(By.CSS_SELECTOR, self.success_popup_css).is_displayed()
        assert element

    def verify_lot_id_checkbox_is_checked(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        time.sleep(5)
        element = context.driver.find_element(By.XPATH, self.lod_id_checkbox_xpath)
        assert element.is_selected()

    def verify_wafer_checkbox_is_checked(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.wafer_checkbox_xpath)
        assert element.is_selected()

    def verify_work_center_is_not_displayed(self, context):
        wait = WebDriverWait(context.driver, 60)
        element = wait.until(EC.invisibility_of_element_located((By.XPATH, self.work_center_xpath)))
        assert element

    def choose_test_program_level_policy(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        wait.until(EC.visibility_of_element_located((By.XPATH, self.test_program_level_policy_xpath))).click()

    def choose_device_level_policy(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        wait.until(EC.visibility_of_element_located((By.XPATH, self.device_level_policy_xpath))).click()

    def click_policy_based_amg_map_btn(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.policy_based_map_btn_id).click()
