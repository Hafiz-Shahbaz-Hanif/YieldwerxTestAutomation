from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AMGMapGenerationsClass:

    def __init__(self):
        pass

    loader = "(//body[@class='loading'])[1]"
    amg_policies_section_title_xpath = "//span[text()='Assembly Map Policies']"
    amg_generations_title_xpath = "//span[text()='Generations']"
    amg_policy_name_column_xpath = "//div[text()='Name']"
    amg_policy_version_column_xpath = "//div[text()='Version']"
    amg_policy_type_column_xpath = "//div[text()='Type']"
    amg_policy_facility_column_xpath = "//div[text()='Facility']"
    amg_policy_work_center_column_xpath = "//div[text()='Work Center']"
    amg_policy_device_column_xpath = "//div[text()='Device']"
    amg_policy_test_program_column_xpath = "//div[text()='Test Program']"
    amg_policy_date_modified_column_xpath = "//div[text()='Date Modified']"
    amg_policy_Successful_column_xpath = "//div[text()='Successful']"
    amg_policy_Failed_column_xpath = "//div[text()='Failed']"
    amg_policy_pending_wafers_column_xpath = "//div[text()='Pending Wafers']"

    amg_policy_name_on_grid_xpath = "//table[@id='PoliciesGrid']/tbody/tr[2]/td[2]"

    def verify_amg_policies_section_title(self, context):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.amg_policies_section_title_xpath)
        assert element.is_displayed()

    def verify_generations_title(self, context):
        element = context.driver.find_element(By.XPATH, self.amg_generations_title_xpath)
        assert element.is_displayed()

    def verify_amg_policy_display_on_generations_tab(self, context, expected_text):
        wait = WebDriverWait(context.driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.amg_policy_name_on_grid_xpath)))
        element = context.driver.find_element(By.XPATH, self.amg_policy_name_on_grid_xpath)
        assert element.text.__eq__(expected_text)

    def verify_amg_policy_section_column_titles(self, context):
        context.driver.find_element(By.XPATH, self.amg_policy_name_column_xpath).is_displayed()
        context.driver.find_element(By.XPATH, self.amg_policy_version_column_xpath).is_displayed()
        context.driver.find_element(By.XPATH, self.amg_policy_type_column_xpath).is_displayed()
        context.driver.find_element(By.XPATH, self.amg_policy_facility_column_xpath).is_displayed()
        context.driver.find_element(By.XPATH, self.amg_policy_work_center_column_xpath).is_displayed()
        context.driver.find_element(By.XPATH, self.amg_policy_device_column_xpath).is_displayed()
        context.driver.find_element(By.XPATH, self.amg_policy_test_program_column_xpath).is_displayed()
        context.driver.find_element(By.XPATH, self.amg_policy_date_modified_column_xpath).is_displayed()
        context.driver.find_element(By.XPATH, self.amg_policy_Successful_column_xpath).is_displayed()
        context.driver.find_element(By.XPATH, self.amg_policy_Failed_column_xpath).is_displayed()
        context.driver.find_element(By.XPATH, self.amg_policy_pending_wafers_column_xpath).is_displayed()



