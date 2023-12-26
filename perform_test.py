import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from datetime import datetime, timedelta
from config import (first_name, first_name_space, first_name_second_user, first_name_capital_letters, last_name_capital_letters, last_name, last_name_space, last_name_second_user, zip_code, zip_code_space, zip_code_invalid, employee_id_small_letter, employee_id, employee_id_space, employee_id_second_user, date_of_birth, date_of_birth_failed, date_of_birth_second_eser, date_of_birth_second_eser_failed, date_of_birth_not_eligible,first_name_under18, last_name_under18, date_of_birth_under18, employee_id_under18, zip_code_under18, first_name_under13, last_name_under13, date_of_birth_under13, employee_id_under13, zip_code_under13)



def setup_driver():
    options = ChromeOptions()
    options.add_argument("-incognito")
    driver = Chrome(options=options)
    return driver

def perform_test(driver):
    # First window
    driver.get('https://portal-lab.limbix.com/onboarding/testsparkfilebasedorg')
    driver.maximize_window()
    action_chains = ActionChains(driver)
    EnvironmentButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-llJcti.jNNNqK')))
    action_chains.double_click(EnvironmentButton).perform()
    EnvironmentButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-llJcti.jNNNqK')))
    action_chains.double_click(EnvironmentButton).perform()
    # Second window
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://portal-lab.limbix.com/onboarding/testsparkfilebasedorg')
    radiobutton_myself = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div > div:nth-child(3) > div:nth-child(1) > label')))
    radiobutton_myself.click()
    check_coverage_button = driver.find_element(By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div > div.sc-aXZVg.CTAButtonstyles__ButtonContainer-sc-172pifp-0.fcpFyo.hnCeuq > button > div')
    check_coverage_button.click()

    # Get elements
    first_name_elem = driver.find_element(By.ID, 'coverageFormFirstName')
    last_name_elem = driver.find_element(By.ID, 'coverageFormLastName')
    zip_code_elem = driver.find_element(By.ID, 'coverageFormZipCode')
    employee_id_elem = driver.find_element(By.ID, 'coverageFormEmployeeId')
    date_of_birth_elem = driver.find_element(By.ID, 'coverageFormDOB')
    check_coverage_button_elem = driver.find_element(By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.sc-aXZVg.CTAButtonstyles__ButtonContainer-sc-172pifp-0.fcpFyo.hnCeuq > button')
    force_eligibility_elem = driver.find_element(By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(13) > span')
    override_eligibility_elem = driver.find_element(By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(12) > span')

    return first_name_elem, last_name_elem, zip_code_elem, employee_id_elem, date_of_birth_elem, check_coverage_button_elem, force_eligibility_elem, override_eligibility_elem

def covered_page(driver):
    first_name_elem, last_name_elem, zip_code_elem, employee_id_elem, date_of_birth_elem, check_coverage_button_elem, force_eligibility_elem, override_eligibility_elem = perform_test(driver)
    first_name_elem.send_keys(first_name_capital_letters)
    last_name_elem.send_keys(last_name_capital_letters)
    zip_code_elem.send_keys(zip_code)
    employee_id_elem.send_keys(employee_id_small_letter)
    date_of_birth_elem.send_keys(date_of_birth)
    check_coverage_button_elem.click()
    time.sleep(2)
    next_button_coverage = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.sc-aXZVg.CTAButtonstyles__ButtonContainer-sc-172pifp-0.fcpFyo.hnCeuq > button')))
    you_are_covered_page_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.sc-aXZVg.sc-eBMEME.fcpFyo.dVszMr')))
    you_are_covered_page_p = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.sc-aXZVg.sc-dCFHLb.fcpFyo.ctYaUb')))
    you_are_covered_page_what = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.sc-aXZVg.sc-hCPjZK.fcpFyo.ipdJds > div.sc-aXZVg.sc-Nxspf.fcpFyo.dVaKcL')))
    you_are_covered_page_answer = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.sc-aXZVg.sc-hCPjZK.fcpFyo.ipdJds > div:nth-child(2) > p')))
    you_are_covered_page_download = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.sc-aXZVg.sc-hCPjZK.fcpFyo.ipdJds > div:nth-child(3) > p')))
    you_are_covered_page_start = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.sc-aXZVg.sc-hCPjZK.fcpFyo.ipdJds > div:nth-child(4) > p')))

    return next_button_coverage, you_are_covered_page_title, you_are_covered_page_p, you_are_covered_page_what, you_are_covered_page_answer, you_are_covered_page_download, you_are_covered_page_start


def sorry_page(driver):
    first_name_elem, last_name_elem, zip_code_elem, employee_id_elem, date_of_birth_elem, check_coverage_button_elem,force_eligibility_elem, override_eligibility_elem = perform_test(driver)
    first_name_elem.send_keys(first_name_capital_letters)
    last_name_elem.send_keys(last_name_capital_letters)
    zip_code_elem.send_keys(zip_code)
    employee_id_elem.send_keys(employee_id_small_letter)
    date_of_birth_elem.send_keys(date_of_birth)
    force_eligibility_elem.click()
    check_coverage_button_elem.click()
    time.sleep(2)
    we_are_sorry_page_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.sc-aXZVg.sc-esYiGF.fcpFyo.HOcMb')))
    first_under_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(2)')))
    second_under_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(3)')))
    experiencing_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(7)')))
    experiencing_first_p = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(8)')))
    experiencing_second_p = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(9)')))
    experiencing_third_p = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(10)')))
    suicide_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(11)')))
    suicide_p = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(12)')))
    suicide_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(12) > a')))
    crisis_text_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(13)')))
    crisis_text_p = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(14)')))
    LGBTQ_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(15)')))
    LGBTQ_p = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(16)')))
    LGBTQ_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(16) > a')))
    poison_control_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(17)')))
    poison_control_p = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(17)')))
    need_support_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(18)')))
    need_support_p = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(20)')))
    need_support_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > a:nth-child(19)')))
    need_support_p_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(22)')))
    need_support_link_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > a:nth-child(21)')))
    need_support_p_3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(24)')))
    need_support_link_3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > a:nth-child(23)')))
    need_support_p_4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > a:nth-child(23)')))

    return we_are_sorry_page_title, first_under_title, second_under_title, experiencing_title, experiencing_first_p, experiencing_second_p, experiencing_third_p, suicide_title, suicide_p, crisis_text_title, crisis_text_p, LGBTQ_title, LGBTQ_p, suicide_link, LGBTQ_link, poison_control_title, poison_control_p, need_support_title, need_support_p, need_support_link, need_support_p_2, need_support_link_2, need_support_p_3, need_support_link_3, need_support_p_4


def about_your_page(driver):
    next_button_coverage, you_are_covered_page_title, you_are_covered_page_p, you_are_covered_page_what, you_are_covered_page_answer, you_are_covered_page_download, you_are_covered_page_start = covered_page(driver)
    next_button_coverage.click()
    time.sleep(2)

    email_elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'patientEmail')))
    phone_number_elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'patientPhoneNumber')))
    street_address_elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'patientStreetAddress')))
    city_elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'patientCity')))
    state_elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'state-select')))
    email_elem_placeholder = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'patientEmail-label')))
    phone_number_placeholder = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'patientPhoneNumber-label')))
    street_address_placeholder = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'patientStreetAddress-label')))
    city_placeholder = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'patientCity-label')))
    state_placeholder = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'state-select-label')))
    acknowledge_checkbox_elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(10) > input')))
    terms_privacy_elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(11) > input')))
    privacy_policy_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.sc-aXZVg.hcgPgx > p')))
    next_button_new = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.sc-aXZVg.CTAButtonstyles__ButtonContainer-sc-172pifp-0.fcpFyo.hnCeuq > button > div')))
    terms_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(11) > label > a:nth-child(1)')))
    privacy_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(11) > label > a:nth-child(2)')))

    return email_elem, phone_number_elem, street_address_elem, city_elem, state_elem, email_elem_placeholder, phone_number_placeholder, street_address_placeholder, city_placeholder, state_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, privacy_policy_link, next_button_new, terms_link, privacy_link