import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


def test_welcome_page():
    options = Options()
    options.add_argument("-incognito")
    driver = webdriver.Chrome(options=options)
    driver.get('https://portal-lab.limbix.com/onboarding/testsparkfilebasedorg')
    driver.maximize_window()
    EnvironmentButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-llJcti.jNNNqK')))
    action_chains = ActionChains(driver)
    action_chains.double_click(EnvironmentButton).perform()
    EnvironmentButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-llJcti.jNNNqK')))
    action_chains.double_click(EnvironmentButton).perform()
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
    radiobutton_myself = driver.find_element(By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div > div:nth-child(3) > div:nth-child(1) > label')
    assert radiobutton_myself.text == expected_radiobutton_myself

    expected_radiobutton_dependent = 'A dependent'
    radiobutton_dependent = driver.find_element(By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div > div:nth-child(3) > div:nth-child(2) > label')
    assert radiobutton_dependent.text == expected_radiobutton_dependent

    check_coverage_button = driver.find_element(By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div > div.sc-aXZVg.CTAButtonstyles__ButtonContainer-sc-172pifp-0.fcpFyo.hnCeuq > button > div')
    assert check_coverage_button != check_coverage_button.is_enabled()
    radiobutton_myself.click()
    assert check_coverage_button.is_enabled()
    radiobutton_dependent.click()
    assert check_coverage_button.is_enabled()
