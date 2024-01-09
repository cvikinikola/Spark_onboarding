import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def driver():
    options = ChromeOptions()
    options.add_argument("-incognito")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()