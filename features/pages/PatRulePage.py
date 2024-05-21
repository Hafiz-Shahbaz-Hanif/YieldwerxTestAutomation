from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class PatRulePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    new_static_pat_rule_window_xpath = "//div[@class='span2 action-nav-button btn-dynamic']//a[@id='btn-dynamic-rule']"
    general_tab_xpath = "//a[@id='general-tab']"
    name_field_xpath = "//input[@id='Rule_Name']"
    parameters_tab_id = "parameter-tab"
    static_limits_tab_id = "initial-limit-tab"
    facility_option_xpath = "//option[@value='WEB SMALL DATASET']"
    workcenter_option_xpath = "//option[@value='WAFER SORT']"
    device_option_xpath = "//option[@value='4670']"
    test_program_option_xpath = "//option[@value='PREBAKE_A_4670']"
    parameter_number_option_xpath = "//tr[@id='1']//td[contains(@title,'26')][contains(text(),'Idd_prewrite Idd_prewrite')]"
    bin_type_dropdown_xpath = "//select[@id='Points_GetBy_IsHardBin']"
    low_seed_limit_id = "Static_PAT_Lo_Limit"
    high_seed_limit_id = "Static_PAT_Hi_Limit"
    calculate_seed_button_id = "btn-calculate-static-seed-limit"
    select_lots_dropdown_id = "Lots"
    calculate_btn_id = "btn-calculate"
    every_lot_field_id = "Notify_LotCount"
    value_of_k_field_id = "Static_Val_K"
    pat_limit_to_apply_dropdown_id = "LimitToApplyId"

    def select_pat_limit_to_apply(self, text_value):
        self.select_dropdown_option("pat_limit_to_apply_dropdown_id", self.pat_limit_to_apply_dropdown_id, text_value)

    def select_lot_option(self, text_value):
        self.select_dropdown_option("select_lots_dropdown_id", self.select_lots_dropdown_id, text_value)

    def select_bin_type_option(self, text_value):
        self.select_dropdown_option("bin_type_dropdown_xpath", self.bin_type_dropdown_xpath, text_value)

    def click_on_parameternumber_option(self):
        self.click_on_element("parameter_number_option_xpath", self.parameter_number_option_xpath)

    def click_on_calculate_seed_button(self):
        self.click_on_element("calculate_seed_button_id", self.calculate_seed_button_id)

    def click_on_lots_calculate_button(self):
        self.click_on_element("calculate_btn_id", self.calculate_btn_id)

    def click_on_testprogram_option(self):
        self.click_on_element("test_program_option_xpath", self.test_program_option_xpath)

    def click_on_device_option(self):
        self.click_on_element("device_option_xpath", self.device_option_xpath)

    def click_on_workcenter_option(self):
        self.click_on_element("workcenter_option_xpath", self.workcenter_option_xpath)

    def click_on_facility_option(self):
        self.click_on_element("facility_option_xpath", self.facility_option_xpath)

    def click_on_parameters_tab(self):
        self.click_on_element("parameters_tab_id", self.parameters_tab_id)

    def click_on_static_limit_tab(self):
        self.click_on_element("static_limits_tab_id", self.static_limits_tab_id)

    def click_on_pat_rule_window(self):
        self.click_on_element("new_static_pat_rule_window_xpath", self.new_static_pat_rule_window_xpath)

    def click_on_general_tab(self):
        self.click_on_element("general_tab_xpath", self.general_tab_xpath)

    def enter_into_name_field(self, name_text):
        self.type_into_element("name_field_xpath", self.name_field_xpath, name_text)

    def enter_into_low_seed_limit_field(self, name_text):
        self.type_into_element("low_seed_limit_id", self.low_seed_limit_id, name_text)

    def enter_into_high_seed_limit_field(self, name_text):
        self.type_into_element("high_seed_limit_id", self.high_seed_limit_id, name_text)

    def enter_into_after_every_lot_field(self, name_text):
        self.type_into_element("every_lot_field_id", self.every_lot_field_id, name_text)

    def enter_into_value_of_k_field(self, name_text):
        self.type_into_element("value_of_k_field_id", self.value_of_k_field_id, name_text)



