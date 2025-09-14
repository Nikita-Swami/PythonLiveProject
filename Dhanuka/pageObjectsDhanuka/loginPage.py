#Login Page Class
from logging import exception

#Page Locators
#Page Actions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Dhanuka.utilsDhanuka.common_utils import WebDriverWait


class LoginPageDhanuka:
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    username = (By.ID, "UserName")
    password = (By.ID, "Password")
    submit_button = (By.XPATH, "//button[@type='submit']")
    error_message = (By.XPATH, "//span[@class='field-validation-error']")

    #forgot_password_button = (By.XPATH, "//a[@class='forgot-password-link']")
    #remember_checkbox = (By.XPATH, "//input[@id='RememberMe']")

    # Page Actions
    def get_username(self):
        return self.driver.find_element(*LoginPageDhanuka.username)

    def get_password(self):
        return self.driver.find_element(*LoginPageDhanuka.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPageDhanuka.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPageDhanuka.error_message)

    #def get_forgot_password_button(self):
    #   return self.driver.find_element(*LoginPageDhanuka.forgot_password_button)

    #def get_remember_checkbox(self):
    #   return self.driver.find_element(*LoginPageDhanuka.remember_checkbox)


    def login_to_dhanuka(self, usr, pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(pwd)
            self.get_submit_button().click()

        except exception as e:
            print(e)


    def get_error_message_text(self):
        return self.get_error_message().text
             #pass



