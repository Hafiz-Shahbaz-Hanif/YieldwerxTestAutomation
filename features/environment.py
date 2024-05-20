import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from behave import *

from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage
from utilities import ConfigReader


def before_scenario(context,driver):

    browser_name = ConfigReader.read_configuration("basic info","browser")

    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info","url"))

    context.login_page = LoginPage(context.driver)
    context.login_page.enter_into_username_field(ConfigReader.read_configuration("credentials","username"))
    context.login_page.enter_into_password_field(ConfigReader.read_configuration("credentials","password"))
    context.login_page.click_on_login_button()
    time.sleep(2)
    context.home_page = HomePage(context.driver)
    assert context.home_page.verify_homepage_heading_text("Realtime SPC Templates")


def after_scenario(context,driver):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_username_link()
    context.home_page.click_on_logout_link()
    context.driver.quit()


def after_step(context,step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name="failed_screenshot"
                      ,attachment_type=AttachmentType.PNG)
