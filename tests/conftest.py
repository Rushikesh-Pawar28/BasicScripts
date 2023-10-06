import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    option.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=option)
    driver.get('https://www.saucedemo.com/v1/')
    request.cls.driver = driver
    yield
    driver.close()
