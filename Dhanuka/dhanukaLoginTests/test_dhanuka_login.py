import allure
import pytest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Assertions and use the Page Object class

# Webdriver Start
# User Interaction + Assertions
# Close Webdriver

#from tests.constants.constants import Constants
from Dhanuka.pageObjectsDhanuka.loginPage import LoginPageDhanuka
from Dhanuka.pageObjectsDhanuka.dashboardPage import DashboardPageDhanuka

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://dhanukadev.prowessbeat.net/")
    return driver


@allure.epic("Dhanuka Login Test")
@allure.feature("TC#0 Dhanuka Negative Test")
@pytest.mark.negative

def test_dhanuka_login_negative(setup):
    login_page= LoginPageDhanuka(driver=setup)
    login_page.login_to_dhanuka(usr="admin", pwd="admin")
    time.sleep(15)
    error_msg_element = login_page.get_error_message_text()
    assert error_msg_element == "The user name or password provided is incorrect."

@allure.epic("Dhanuka Login Test")
@allure.feature("TC#1 Dhanuka Positive Test")
@pytest.mark.positive

def test_dhanuka_login_positive(setup):
    login_page = LoginPageDhanuka(driver=setup)
    login_page.login_to_dhanuka(usr="Portaladmin", pwd="Port@123")
    time.sleep(15)
    dashboardPage = DashboardPageDhanuka(driver=setup)
    assert "FDFR Current Week" in dashboardPage.user_logged_in_text()


