import allure
import pytest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import org.openqa.selenium.InvalidSelectorException;
# Assertions and use the Page Object class

# Webdriver Start
# User Interaction + Assertions
# Close Webdriver

from Dhanuka.pageObjectsDhanuka.loginPage import LoginPageDhanuka
from Dhanuka.pageObjectsDhanuka.dashboardPage import DashboardPageDhanuka
from Dhanuka.pageObjectsDhanuka.customermasterPage import CustomerMasterPageDhanuka

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://dhanukadev.prowessbeat.net/")
    return driver

@allure.epic("Dhanuka Login Test")
@allure.feature("TC#1 Dhanuka Positive Test")
@pytest.mark.positive

def test_dhanuka_customer(setup):
    login_page = LoginPageDhanuka(driver=setup)
    login_page.login_to_dhanuka(usr="Portaladmin", pwd="Port@123")
    #time.sleep(10)
    #dashboardPage = DashboardPageDhanuka(driver=setup)
    #assert "FDFR Current Week" in dashboardPage.user_logged_in_text()
    main_masterPage =CustomerMasterPageDhanuka(driver=setup)
    main_masterPage.get_master_page()
    time.sleep(10)

    customer_masterPage = CustomerMasterPageDhanuka(driver=setup)
    customer_masterPage.get_customer_master_page()
    time.sleep(10)

    customers_Page = CustomerMasterPageDhanuka(driver=setup)
    customers_Page.get_customers()
    time.sleep(10)

    add_customer_form_Page = CustomerMasterPageDhanuka(driver=setup)
    add_customer_form_Page.get_add_retailer()
    time.sleep(10)

    add_customer_form_details = CustomerMasterPageDhanuka(driver=setup)
    add_customer_form_details.get_add_retailer_details(cust_code="AutoRet001",cust_name="Auto Retailer001",div_id="123")
    time.sleep(60)
