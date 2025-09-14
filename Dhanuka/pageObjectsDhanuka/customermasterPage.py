# Customer Master Page Class

# Page Locators
# Page Actions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Dhanuka.pageObjectsDhanuka.dashboardPage import DashboardPageDhanuka
from Dhanuka.utilsDhanuka.common_utils import webdriver_wait


class CustomerMasterPageDhanuka:
    def __init__(self, driver):
        self.driver = driver

    user_logged_in = (By.XPATH, "//div[@class='main-container-inner']")
    main_master = (By.XPATH, "//a[@id='tooltip3']")
    customer = (By.XPATH, "//div/div/div/div/ul/li/a/span[text()='Customer']")

    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPageDhanuka.user_logged_in)

    def get_master_page(self):
        return self.driver.find_element(*CustomerMasterPageDhanuka.main_master)

