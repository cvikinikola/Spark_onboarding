import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from conftest import driver

def test_welcome_page():
    options = Options()
    options.add_argument("-incognito")
    driver = webdriver.Chrome(options=options)
    driver.get('https://portal-lab.limbix.com/onboarding/testsparkfilebasedorg')
    driver.maximize_window()
    environment_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-jsJBEP.gsixxv')))
    action_chains = ActionChains(driver)
    action_chains.double_click(environment_button).perform()
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://portal-lab.limbix.com/onboarding/testsparkfilebasedorg')

    expected_title = 'Welcome! Are you enrolling yourself or a dependent?'
    title_text = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-eBMEME.fcpFyo.dVszMr')
    assert title_text.text == expected_title

    expected_p_text = "Check if Spark Direct is covered by your insurance or employer. If you're under the age of 18, please have a caretaker complete this step."
    p_text = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-dCFHLb.fcpFyo.ctYaUb')
    assert p_text.text == expected_p_text

    expected_radiobutton_myself = 'Myself'
    radiobutton_myself = driver.find_element(By.CSS_SELECTOR, '[for="enrollmentPersonpatient"]')
    assert radiobutton_myself.text == expected_radiobutton_myself

    expected_radiobutton_dependent = 'A dependent'
    radiobutton_dependent = driver.find_element(By.CSS_SELECTOR, '[for="enrollmentPersoncaregiver"]')
    assert radiobutton_dependent.text == expected_radiobutton_dependent

    check_coverage_button = driver.find_element(By.XPATH, "//button[@disabled][contains(@class, 'CTAButtonstyles__Button')]")
    assert check_coverage_button != check_coverage_button.is_enabled()
    radiobutton_myself.click()
    assert check_coverage_button.is_enabled()
    radiobutton_dependent.click()
    assert check_coverage_button.is_enabled()
