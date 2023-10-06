from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self,driver):
        self.driver = driver

    products = (By.XPATH, '//div[@class="inventory_item"]')
    cartbtn = (By.XPATH, '//a[@class="shopping_cart_link fa-layers fa-fw"]')

    def AllProducts(self):
        return self.driver.find_elements(*ProductPage.products)

    def CartBtn(self):
        return self.driver.find_element(*ProductPage.cartbtn)