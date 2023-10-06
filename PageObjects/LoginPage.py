from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    username = (By.CSS_SELECTOR, '#user-name')
    password = (By.CSS_SELECTOR, '#password')
    loginBtn = (By.CSS_SELECTOR, '#login-button')

    def userName(self):
        return self.driver.find_element(*LoginPage.username)

    def passWord(self):
        return self.driver.find_element(*LoginPage.password)

    def LoginBtn(self):
        return self.driver.find_element(*LoginPage.loginBtn)
