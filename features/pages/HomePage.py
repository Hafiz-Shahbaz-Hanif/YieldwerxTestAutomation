from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    homepage_heading_xpath = "//div[@class='pull-left header']"
    quality_and_pat_xpath = "//span[normalize-space()='Quality & PAT']"
    username_dropdown_xpath = "//span[normalize-space()='Michael Justin']//i[@class='icon-caret-down']"
    logout_link_xpath = "//span[normalize-space()='Logout']"
    pat_rule_heading_xpath = "//a[@href='/Rules']"
    pat_heading_xpath = "//span[normalize-space()='PAT']"

    def click_on_logout_link(self):
        self.click_on_element("logout_link_xpath", self.logout_link_xpath)

    def click_on_username_link(self):
        self.click_on_element("username_dropdown_xpath", self.username_dropdown_xpath)

    def verify_homepage_heading_text(self, expected_text):
        return self.retrieved_element_text_contains("homepage_heading_xpath", self.homepage_heading_xpath,                                                    expected_text)

    def verify_quality_and_pat_text(self, expected_text):
        return self.retrieved_element_text_contains("quality_and_pat_xpath", self.quality_and_pat_xpath,                                                    expected_text)

    def click_quality_and_pat_heading(self):
        self.click_on_element("quality_and_pat_xpath", self.quality_and_pat_xpath)

    def click_pat_heading(self):
        self.click_on_element("pat_heading_xpath", self.pat_heading_xpath)

    def click_pat_rule_heading(self):
        self.click_on_element("pat_rule_heading_xpath", self.pat_rule_heading_xpath)

