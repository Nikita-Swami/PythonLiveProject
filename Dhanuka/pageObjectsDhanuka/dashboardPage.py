#Dashboard Page Class

#Page Locators
#Page Actions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Dhanuka.utilsDhanuka.common_utils import webdriver_wait

class DashboardPageDhanuka:
    def __init__(self,driver):
        self.driver = driver

    user_logged_in = (By.XPATH,"//div[@class='main-container-inner']")

    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPageDhanuka.user_logged_in)

    def user_logged_in_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.user_logged_in,timeout=15)
        return self.get_user_logged_in().text
