from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    testbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//*[@type='submit']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setuserName(self, username):
        self.driver.find_element(By.ID, self.testbox_username_id).clear()
        self.driver.find_element(By.ID, self.testbox_username_id).send_keys(username)

    def setPassWord(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
        # self.driver.find_element_by_id(self.textbox_password_id).clear()
        # self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
