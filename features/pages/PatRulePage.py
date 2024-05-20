from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class PatRulePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    new_static_pat_rule_window_xpath = "//div[@class='span2 action-nav-button btn-dynamic']//a[@id='btn-dynamic-rule']"

    def click_on_pat_rule_window(self):
        self.click_on_element("new_static_pat_rule_window_xpath", self.new_static_pat_rule_window_xpath)



