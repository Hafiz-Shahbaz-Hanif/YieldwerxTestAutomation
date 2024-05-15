from features.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username_id = "UserName"
    password_id = "Password"
    login_button_id = "login-button"
    homepage_heading_xpath = "//div[@class='pull-left header']"

    def enter_into_username_field(self, username_text):
        self.type_into_element("username_id", self.username_id, username_text)

    def enter_into_password_field(self, password_text):
        self.type_into_element("password_id", self.password_id, password_text)

    def click_on_login_button(self):
        self.click_on_element("login_button_id", self.login_button_id)

    def verify_homepage_heading_text(self, expected_text):
        return self.retrieved_element_text_contains("homepage_heading_xpath", self.homepage_heading_xpath,                                                    expected_text)
