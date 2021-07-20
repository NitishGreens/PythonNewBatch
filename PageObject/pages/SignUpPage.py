from selenium.webdriver.common.by import By
from PageObject import Locators


class SignUpPage:
    def __init__(self, driver):
        self.txt_fname = driver.find_element(By.NAME, Locators.first_name_name)
        self.txt_lname = driver.find_element(By.NAME, Locators.surname_name)

    # getters
    def getTxtFirstName(self):
        return self.txt_fname

    def getTxtLastName(self):
        return self.txt_lname
