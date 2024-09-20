import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utilities import ConfigReader
from utilities.customLogger import LogGen


class LoginClass:
    logger = LogGen.loggen()

    def __init__(self):
        pass

    ttl = "//span[@class='title']"
    loader = "(//body[@class='loading'])[1]"
    username_xpath = "//input[@id='UserName']"
    password_id = "Password"
    dashboard_title_xpath = "(//h3[normalize-space() = 'Realtime SPC Templates'])[1]"

    def launchBrowser(self, context):
        browser_name = ConfigReader.read_configuration("basic info", "browser")

        if browser_name.__eq__("chrome"):
            context.driver = webdriver.Chrome()
        elif browser_name.__eq__("headless"):
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("user-agent=your-user-agent-string")
            context.driver = webdriver.Chrome(options=options)
        elif browser_name.__eq__("firefox"):
            context.driver = webdriver.Firefox()
        elif browser_name.__eq__("edge"):
            context.driver = webdriver.Edge()

        context.driver.maximize_window()
        self.logger.info("**********  Browser Launched Successfully  **********")

    def openWebsite(self, context):
        context.driver.get(ConfigReader.read_configuration("basic info", "url"))
        # self.logger.info("**********  Trying to Open Link  **********")
        context.driver.maximize_window()
        self.logger.info("**********  Maximize Window  **********")
        # self.wait_for_element_visible(By.XPATH, "//span[@class='title']")
        self.logger.info("**********  Wait for Title  **********")

    def verifyLoginPageOpened(self, context):
        status = context.driver.find_element(By.XPATH, self.ttl).is_displayed()
        assert status is True
        self.logger.info("**********  Login Screen Opened Successfully  **********")

    def enterUsernamePassword(self, context):
        context.driver.find_element(By.XPATH, self.username_xpath).send_keys(ConfigReader.read_configuration("credentials",
                                                                                                   "username"))
        context.driver.find_element(By.ID, self. password_id).send_keys(ConfigReader.read_configuration("credentials",
                                                                                                   "password"))
        self.logger.info("**********  Entered UserName & Password Successfully  **********")

    def enterCredentials(self, context):
        context.driver.find_element(By.XPATH, self.username_xpath).send_keys(ConfigReader.read_configuration(
            "credentials","username"))
        context.driver.find_element(By.ID, self.password_id).send_keys(ConfigReader.read_configuration("credentials",
                                                                                                 "username"))
        self.logger.info("**********  Entered UserName & Password Successfully  **********")

    def hitLoginButton(self, context):
        context.driver.find_element(By.ID, "login-button").click()
        self.logger.info("**********  Clicked the Login button  **********")

    def verifyDashboard(self, context):
        WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        status = context.driver.find_element(By.XPATH, self.dashboard_title_xpath).is_displayed()
        assert status is True
        self.logger.info("**********  Dashboard displayed successfully  **********")

    def quiteBrowser(self, context):
        context.driver.close()
        context.driver.quit()
        self.logger.info("**********  Browser Closed  **********")
