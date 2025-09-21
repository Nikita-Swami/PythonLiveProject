# Customer Master Page Class
from selenium.common import InvalidSelectorException
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

    #user_logged_in = (By.XPATH, "//div[@class='main-container-inner']")
    main_master = (By.XPATH, "//a[@id='tooltip3']")
    customer_master = (By.XPATH, "//div/div/div/div/ul/li/a/span[text()='Customer']")
    customers = (By.XPATH, "//a[@href='/CustomerMaster/GetCustomerMaster/6018']")
    #add customer form
    add_customer_button = (By.XPATH,"//button[@id='btnAdd']")
    #all forms fields
    customer_code = (By.XPATH,"//input[@name='SLCODE']")
    customer_name = (By.XPATH,"//input[@id='NAME']")
    division_id = (By.XPATH, "//input[@id='DIVISIONROWID']")
    customer_dd = (By.XPATH, "//div[@id='select2-drop-mask']")
    customer_type_dd = (By.XPATH,"//div[@id='s2id_SLTYPEID']//span[contains(text(), 'Retailer')]")
    parent_dd = (By.XPATH, "//div[@id='s2id_PID']")


    #def get_user_logged_in(self):
     #   return self.driver.find_element(*DashboardPageDhanuka.user_logged_in)

    #def user_logged_in_text(self):
    #    webdriver_wait(driver=self.driver, element_tuple=self.user_logged_in, timeout=15)
      #  return self.get_user_logged_in().text

    #Go to Master
    def get_master_page(self):
        self.driver.find_element(*CustomerMasterPageDhanuka.main_master).click()


    def user_customer_in_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.main_master, timeout=15)
        self.get_master_page()

    # Click On Customer
    def get_customer_master_page(self):
        self.driver.find_element(*CustomerMasterPageDhanuka.customer_master).click()

    def user_customer_master_in_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.customer_master, timeout=15)
        self.get_customer_master_page()


    #Click on Customer Menu
    def get_customers(self):
        self.driver.find_element(*CustomerMasterPageDhanuka.customers).click()

    def user_customers(self):
        webdriver_wait(driver=self.driver, element_tuple=self.customers, timeout=15)
        self.get_customers()

    #Add new Customer
    def get_add_retailer(self):
        webdriver_wait(driver=self.driver, element_tuple=self.add_customer_button, timeout=15)
        self.driver.find_element(*CustomerMasterPageDhanuka.add_customer_button).click()


    def get_add_retailer_details(self,cust_code,cust_name,div_id):
        try:
            webdriver_wait(driver=self.driver, element_tuple=self.customer_code, timeout=15)
            self.driver.find_element(*CustomerMasterPageDhanuka.customer_code).send_keys(cust_code)

            webdriver_wait(driver=self.driver,element_tuple=self.customer_name, timeout=15)
            self.driver.find_element(*CustomerMasterPageDhanuka.customer_name).send_keys(cust_name)

            webdriver_wait(driver=self.driver, element_tuple=self.division_id, timeout=15)
            self.driver.find_element(*CustomerMasterPageDhanuka.division_id).send_keys(div_id)

            webdriver_wait(driver=self.driver, element_tuple=self.customer_dd, timeout=70)
            self.driver.find_element(*CustomerMasterPageDhanuka.customer_dd).click()

            webdriver_wait(driver=self.driver, element_tuple=self.customer_type_dd, timeout=75)
            self.driver.find_element(*CustomerMasterPageDhanuka.customer_type_dd).click()

        except InvalidSelectorException as e:
            print(e)







