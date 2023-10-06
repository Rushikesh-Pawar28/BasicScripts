import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ProductPage import ProductPage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        self.driver.implicitly_wait(5)

        loginPageObj = LoginPage(self.driver)
        loginPageObj.userName().send_keys('standard_user')
        loginPageObj.passWord().send_keys('secret_sauce')
        loginPageObj.LoginBtn().click()

        productPageObj = ProductPage(self.driver)
        products = productPageObj.AllProducts()
        for product in products:
            product_Names = product.find_element(By.XPATH, '//div[@class="inventory_item"]/div/a/div')
            if product_Names.text == "Sauce Labs Bolt T-Shirt":
                btn = self.driver.find_element(By.XPATH, '//button[@class="btn_primary btn_inventory"]')
                btn.click()

        productPageObj.CartBtn().click()

        checkoutPageObj = CheckOutPage(self.driver)
        checkoutPageObj.CheckOutBtn().click()
        checkoutPageObj.firstName().send_keys("Rushikesh")
        checkoutPageObj.lastName().send_keys("Pawar")
        checkoutPageObj.postalCode().send_keys("431503")
        checkoutPageObj.cartBtn().click()
        checkoutPageObj.finishBtn().click()
        assert "THANK YOU FOR YOUR ORDER" == checkoutPageObj.Msg().text


