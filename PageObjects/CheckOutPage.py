from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    checkoutBtn = (By.XPATH, '//a[@class="btn_action checkout_button"]')
    firstname = (By.CSS_SELECTOR, '#first-name')
    lastname = (By.CSS_SELECTOR, '#last-name')
    postalcode = (By.CSS_SELECTOR, '#postal-code')
    cartbtn = (By.CSS_SELECTOR, '.btn_primary.cart_button')
    finishbtn = (By.CSS_SELECTOR, '.btn_action.cart_button')
    msg = (By.TAG_NAME, 'h2')

    def CheckOutBtn(self):
        return self.driver.find_element(*CheckOutPage.checkoutBtn)

    def firstName(self):
        return self.driver.find_element(*CheckOutPage.firstname)

    def lastName(self):
        return self.driver.find_element(*CheckOutPage.lastname)

    def postalCode(self):
        return self.driver.find_element(*CheckOutPage.postalcode)

    def cartBtn(self):
        return self.driver.find_element(*CheckOutPage.cartbtn)

    def finishBtn(self):
        return self.driver.find_element(*CheckOutPage.finishbtn)

    def Msg(self):
        return self.driver.find_element(*CheckOutPage.msg)
