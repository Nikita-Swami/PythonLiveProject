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

from Dhanuka.pageObjectsDhanuka.loginPage import LoginPageDhanuka
from Dhanuka.pageObjectsDhanuka.dashboardPage import DashboardPageDhanuka
from Dhanuka.pageObjectsDhanuka.customermasterPage import CustomerMasterPageDhanuka

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://dhanukadev.prowessbeat.net/")
    return driver

