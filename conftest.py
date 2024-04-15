import pytest
from selenium import webdriver
import URLS


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(URLS.main_url)
    yield chrome_driver
    chrome_driver.quit()