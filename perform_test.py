import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from config import (first_name, first_name_space, first_name_second_user, first_name_capital_letters, last_name_capital_letters, last_name, last_name_space, last_name_second_user, zip_code, zip_code_space, zip_code_invalid, employee_id_small_letter, employee_id, employee_id_space, employee_id_second_user, date_of_birth, street_address, city, phone_number, email, new_user_email, date_of_birth_second_eser)
from conftest import driver


def first_page(driver):
    # First window
    driver.get('https://portal.limbix.com/onboarding/testsparkfilebasedorg')
    driver.maximize_window()
    action_chains = ActionChains(driver)
    # environment_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-jsJBEP.gsixxv')))
    # action_chains.double_click(environment_button).perform()
    # environment_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-llJcti.jNNNqK')))
    # action_chains.double_click(environment_button).perform()
    # Second window
    # driver.execute_script("window.open('', '_blank');")
    # driver.switch_to.window(driver.window_handles[1])
    # driver.get('https://portal-lab.limbix.com/onboarding/testsparkfilebasedorg')
    # driver.switch_to.window(driver.window_handles[0])
    # driver.close()
    # driver.switch_to.window(driver.window_handles[0])
    radiobutton_myself = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'enrollmentPersonpatient')))
    radiobutton_dependent = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'enrollmentPersoncaregiver')))
    check_coverage_button = driver.find_element(By.XPATH, "//button[@disabled][contains(@class, 'CTAButtonstyles__Button')]")

    return radiobutton_myself, radiobutton_dependent, check_coverage_button

def dependent_flow(driver):
    radiobutton_myself, radiobutton_dependent, check_coverage_button = first_page(driver)
    radiobutton_dependent.click()
    check_coverage_button.click()
    # Get elements
    first_name_elem = driver.find_element(By.ID, 'coverageFormFirstName')
    last_name_elem = driver.find_element(By.ID, 'coverageFormLastName')
    zip_code_elem = driver.find_element(By.ID, 'coverageFormZipCode')
    employee_id_elem = driver.find_element(By.ID, 'coverageFormEmployeeId')
    date_of_birth_elem = driver.find_element(By.ID, 'coverageFormDOB')
    first_name_label = driver.find_element(By.ID, 'coverageFormFirstName-label')
    last_name_label = driver.find_element(By.ID, 'coverageFormLastName-label')
    zip_code_label = driver.find_element(By.ID, 'coverageFormZipCode-label')
    employee_id_label = driver.find_element(By.ID, 'coverageFormEmployeeId-label')
    date_of_birth_label = driver.find_element(By.ID, 'coverageFormDOB-label')
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[@disabled][contains(@class, 'CTAButtonstyles__Button')]")
    checkbox_elements = driver.find_elements(By.CLASS_NAME, 'jss8.MuiSwitch-input')
    # override_eligibility_elem = checkbox_elements[0]
    # force_eligibility_elem = checkbox_elements[1]

    return first_name_elem, last_name_elem, zip_code_elem, employee_id_elem, date_of_birth_elem, first_name_label, last_name_label, zip_code_label, employee_id_label, date_of_birth_label, check_coverage_button_elem  # force_eligibility_elem, override_eligibility_elem

def myself_flow(driver):
    radiobutton_myself, radiobutton_dependent, check_coverage_button = first_page(driver)
    radiobutton_myself.click()
    check_coverage_button.click()
    # Get elements
    first_name_elem = driver.find_element(By.ID, 'coverageFormFirstName')
    last_name_elem = driver.find_element(By.ID, 'coverageFormLastName')
    zip_code_elem = driver.find_element(By.ID, 'coverageFormZipCode')
    employee_id_elem = driver.find_element(By.ID, 'coverageFormEmployeeId')
    date_of_birth_elem = driver.find_element(By.ID, 'coverageFormDOB')
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[@disabled][contains(@class, 'CTAButtonstyles__Button')]")
    checkbox_elements = driver.find_elements(By.CLASS_NAME, 'jss8.MuiSwitch-input')
    # override_eligibility_elem = checkbox_elements[0]
    # force_eligibility_elem = checkbox_elements[1]

    return first_name_elem, last_name_elem, zip_code_elem, employee_id_elem, date_of_birth_elem, check_coverage_button_elem  # force_eligibility_elem, override_eligibility_elem

def covered_page(driver):
    first_name_elem, last_name_elem, zip_code_elem, employee_id_elem, date_of_birth_elem, check_coverage_button_elem = myself_flow(driver)
    first_name_elem.send_keys(first_name_capital_letters)
    last_name_elem.send_keys(last_name_capital_letters)
    zip_code_elem.send_keys(zip_code)
    employee_id_elem.send_keys(employee_id_small_letter)
    date_of_birth_elem.send_keys(date_of_birth)
    check_coverage_button_elem.click()
    time.sleep(2)
    next_button_coverage = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")))
    you_are_covered_page_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-eBMEME.fcpFyo.dVszMr')
    you_are_covered_page_p = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-dCFHLb.fcpFyo.ctYaUb')
    you_are_covered_page_what = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-Nxspf.fcpFyo.dVaKcL')
    you_are_covered_page_answer = driver.find_element(By.XPATH, '//p[@class="sc-gEvEer fixEOS" and contains(text(), "Answer several questions")]')
    you_are_covered_page_download = driver.find_element(By.XPATH, '//p[@class="sc-gEvEer fixEOS" and contains(text(), "Download the Spark Direct")]')
    you_are_covered_page_start = driver.find_element(By.XPATH, '//p[@class="sc-gEvEer fixEOS" and contains(text(), "Start seeing the benefits")]')

    return next_button_coverage, you_are_covered_page_title, you_are_covered_page_p, you_are_covered_page_what, you_are_covered_page_answer, you_are_covered_page_download, you_are_covered_page_start

def covered_page_dependent(driver):
    first_name_elem, last_name_elem, zip_code_elem, employee_id_elem, date_of_birth_elem, first_name_label, last_name_label, zip_code_label, employee_id_label, date_of_birth_label, check_coverage_button_elem = dependent_flow(driver)
    first_name_elem.send_keys(first_name_capital_letters)
    last_name_elem.send_keys(last_name_capital_letters)
    zip_code_elem.send_keys(zip_code)
    employee_id_elem.send_keys(employee_id_small_letter)
    date_of_birth_elem.send_keys(date_of_birth)
    check_coverage_button_elem.click()
    time.sleep(2)
    next_button_coverage = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")))
    you_are_covered_page_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-eBMEME.fcpFyo.dVszMr')
    you_are_covered_page_p = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-dCFHLb.fcpFyo.ctYaUb')
    you_are_covered_page_what = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-Nxspf.fcpFyo.dVaKcL')
    you_are_covered_page_answer = driver.find_element(By.XPATH, '//p[@class="sc-gEvEer fixEOS" and contains(text(), "You will answer several questions")]')
    you_are_covered_page_download = driver.find_element(By.XPATH, '//p[@class="sc-gEvEer fixEOS" and contains(text(), "Your dependent will download the")]')
    you_are_covered_page_start = driver.find_element(By.XPATH, '//p[@class="sc-gEvEer fixEOS" and contains(text(), "They can start seeing benefits")]')

    return next_button_coverage, you_are_covered_page_title, you_are_covered_page_p, you_are_covered_page_what, you_are_covered_page_answer, you_are_covered_page_download, you_are_covered_page_start

def sorry_page(driver):
    first_name_elem, last_name_elem, zip_code_elem, employee_id_elem, date_of_birth_elem, check_coverage_button_elem = myself_flow(driver)
    first_name_elem.send_keys(first_name_capital_letters)
    last_name_elem.send_keys(last_name_capital_letters)
    zip_code_elem.send_keys(zip_code)
    employee_id_elem.send_keys(employee_id_small_letter)
    date_of_birth_elem.send_keys(date_of_birth_second_eser)
    check_coverage_button_elem.click()
    time.sleep(2)
    we_are_sorry_page_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-aXZVg.sc-esYiGF.fcpFyo.HOcMb')))
    first_under_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "not eligible for Spark Direct")]')
    second_under_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "If you have any questions")]')
    experiencing_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-fXSgeo fcpFyo jdDRKE" and contains(text(), "Experiencing a mental health")]')
    experiencing_first_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "If you are currently experiencing")]')
    experiencing_second_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "You can also call or text 988")]')
    experiencing_third_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "If you are not in immediate danger")]')
    suicide_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-fjvvzt fcpFyo kMrRzy" and contains(text(), "988 Suicide and Crisis Lifeline")]')
    suicide_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "Call 988")]')
    suicide_second_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "For deaf or hard of hearing ASL users")]')
    suicide_link = driver.find_element(By.CSS_SELECTOR, '[href^="https://988lifeline.org/chat/"]')
    crisis_text_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-fjvvzt fcpFyo kMrRzy" and contains(text(), "Crisis Text Line")]')
    crisis_text_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "Text HOME to 741741")]')
    LGBTQ_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-fjvvzt fcpFyo kMrRzy" and contains(text(), "The Trevor Project")]')
    LGBTQ_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "Call 1-866-488-7386")]')
    LGBTQ_link = driver.find_element(By.CSS_SELECTOR, '[href^="https://www.thetrevorproject.org/get-help/"]')
    poison_control_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-fjvvzt fcpFyo kMrRzy" and contains(text(), "Poison Control:")]')
    poison_control_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "Call 1-800-222-1222")]')

    need_support_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-fXSgeo fcpFyo jdDRKE" and contains(text(), "If you need support,")]')
    need_support_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "This website can help")]')
    need_support_link = driver.find_element(By.CSS_SELECTOR, '[href^="https://findtreatment.gov/"]')
    need_support_p_2 = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "NAFC can help")]')
    need_support_link_2 = driver.find_element(By.CSS_SELECTOR, '[href^="https://nafcclinics.org/find-clinic/"]')
    need_support_p_3 = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "This site can connect you to low-cost")]')
    need_support_link_3 = driver.find_element(By.CSS_SELECTOR, '[href^="https://www.findhelp.org/"]')
    need_support_p_4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "Big Health is not responsible for any")]')))

    return we_are_sorry_page_title, first_under_title, second_under_title, experiencing_title, experiencing_first_p, experiencing_second_p, experiencing_third_p, suicide_title, suicide_p, crisis_text_title, crisis_text_p, LGBTQ_title, LGBTQ_p, suicide_link, LGBTQ_link, poison_control_title, poison_control_p, need_support_title, need_support_p, need_support_link, need_support_p_2, need_support_link_2, need_support_p_3, need_support_link_3, need_support_p_4, suicide_second_p

def dependent_sorry_page(driver):
    first_name_elem, last_name_elem, zip_code_elem, employee_id_elem, date_of_birth_elem, first_name_label, last_name_label, zip_code_label, employee_id_label, date_of_birth_label, check_coverage_button_elem = dependent_flow(driver)
    first_name_elem.send_keys(first_name_capital_letters)
    last_name_elem.send_keys(last_name_capital_letters)
    zip_code_elem.send_keys(zip_code)
    employee_id_elem.send_keys(employee_id_small_letter)
    date_of_birth_elem.send_keys(date_of_birth_second_eser)
    check_coverage_button_elem.click()
    time.sleep(2)
    we_are_sorry_page_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-aXZVg.sc-esYiGF.fcpFyo.HOcMb')))
    first_under_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "not eligible for Spark Direct")]')
    second_under_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "If you have any questions")]')
    experiencing_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-fXSgeo fcpFyo jdDRKE" and contains(text(), "Experiencing a mental health")]')
    experiencing_first_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "If you are currently experiencing")]')
    experiencing_second_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "You can also call or text 988")]')
    experiencing_third_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "If you are not in immediate danger")]')
    suicide_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-fjvvzt fcpFyo kMrRzy" and contains(text(), "988 Suicide and Crisis Lifeline")]')
    suicide_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "Call 988")]')
    suicide_second_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "For deaf or hard of hearing ASL users")]')
    suicide_link = driver.find_element(By.CSS_SELECTOR, '[href^="https://988lifeline.org/chat/"]')
    crisis_text_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-fjvvzt fcpFyo kMrRzy" and contains(text(), "Crisis Text Line")]')
    crisis_text_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "Text HOME to 741741")]')
    LGBTQ_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-fjvvzt fcpFyo kMrRzy" and contains(text(), "The Trevor Project")]')
    LGBTQ_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "Call 1-866-488-7386")]')
    LGBTQ_link = driver.find_element(By.CSS_SELECTOR, '[href^="https://www.thetrevorproject.org/get-help/"]')
    poison_control_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-fjvvzt fcpFyo kMrRzy" and contains(text(), "Poison Control:")]')
    poison_control_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "Call 1-800-222-1222")]')
    need_support_title = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-fXSgeo fcpFyo jdDRKE" and contains(text(), "If you need support,")]')
    need_support_p = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "This website can help")]')
    need_support_link = driver.find_element(By.CSS_SELECTOR, '[href^="https://findtreatment.gov/"]')
    need_support_p_2 = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "NAFC can help")]')
    need_support_link_2 = driver.find_element(By.CSS_SELECTOR, '[href^="https://nafcclinics.org/find-clinic/"]')
    need_support_p_3 = driver.find_element(By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "This site can connect you to low-cost")]')
    need_support_link_3 = driver.find_element(By.CSS_SELECTOR, '[href^="https://www.findhelp.org/"]')
    need_support_p_4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="sc-aXZVg sc-bbSZdi fcpFyo ledPWQ" and contains(text(), "Big Health is not responsible for any")]')))

    return we_are_sorry_page_title, first_under_title, second_under_title, experiencing_title, experiencing_first_p, experiencing_second_p, experiencing_third_p, suicide_title, suicide_p, crisis_text_title, crisis_text_p, LGBTQ_title, LGBTQ_p, suicide_link, LGBTQ_link, poison_control_title, poison_control_p, need_support_title, need_support_p, need_support_link, need_support_p_2, need_support_link_2, need_support_p_3, need_support_link_3, need_support_p_4, suicide_second_p

def about_your_page(driver):
    next_button_coverage, you_are_covered_page_title, you_are_covered_page_p, you_are_covered_page_what, you_are_covered_page_answer, you_are_covered_page_download, you_are_covered_page_start = covered_page(driver)
    next_button_coverage.click()
    time.sleep(2)

    email_elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'patientEmail')))
    phone_number_elem = driver.find_element(By.ID, 'patientPhoneNumber')
    street_address_elem = driver.find_element(By.ID,  'patientStreetAddress')
    city_elem = driver.find_element(By.ID, 'patientCity')
    state_elem = driver.find_element(By.ID, 'state-select')
    email_elem_placeholder = driver.find_element(By.ID, 'patientEmail-label')
    phone_number_placeholder = driver.find_element(By.ID, 'patientPhoneNumber-label')
    street_address_placeholder = driver.find_element(By.ID, 'patientStreetAddress-label')
    city_placeholder = driver.find_element(By.ID, 'patientCity-label')
    state_placeholder = driver.find_element(By.ID,  'state-select-label')
    checkbox_elements = driver.find_elements(By.CLASS_NAME, 'sc-jxOSlx.gDdgcU')
    acknowledge_checkbox_elem = checkbox_elements[0]
    terms_privacy_elem = checkbox_elements[1]
    privacy_policy_link = driver.find_element(By.XPATH, '//a[@class="sc-tagGq ivXcxM" and contains(text(), "Privacy Policy")]')
    next_button_new = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    terms_link = driver.find_element(By.XPATH, '//a[@class="sc-kdBSHD fGMyTe" and contains(text(), "Terms")]')
    privacy_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="sc-kdBSHD fGMyTe" and contains(text(), "Privacy Policy")]')))

    return email_elem, phone_number_elem, street_address_elem, city_elem, state_elem, email_elem_placeholder, phone_number_placeholder, street_address_placeholder, city_placeholder, state_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, privacy_policy_link, next_button_new, terms_link, privacy_link

def about_dependent_page(driver):
    next_button_coverage, you_are_covered_page_title, you_are_covered_page_p, you_are_covered_page_what, you_are_covered_page_answer, you_are_covered_page_download, you_are_covered_page_start = covered_page_dependent(driver)
    next_button_coverage.click()
    time.sleep(2)

    email_elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'patientEmail')))
    phone_number_elem = driver.find_element(By.ID, 'patientPhoneNumber')
    street_address_elem = driver.find_element(By.ID,  'patientStreetAddress')
    city_elem = driver.find_element(By.ID, 'patientCity')
    state_elem = driver.find_element(By.ID, 'state-select')
    email_elem_placeholder = driver.find_element(By.ID, 'patientEmail-label')
    phone_number_placeholder = driver.find_element(By.ID, 'patientPhoneNumber-label')
    street_address_placeholder = driver.find_element(By.ID, 'patientStreetAddress-label')
    city_placeholder = driver.find_element(By.ID, 'patientCity-label')
    state_placeholder = driver.find_element(By.ID,  'state-select-label')
    next_button_new = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")

    return email_elem, phone_number_elem, street_address_elem, city_elem, state_elem, email_elem_placeholder, phone_number_placeholder, street_address_placeholder, city_placeholder, state_placeholder, next_button_new

def caregiver_page(driver):
    email_elem, phone_number_elem, street_address_elem, city_elem, state_elem, email_elem_placeholder, phone_number_placeholder, street_address_placeholder, city_placeholder, state_placeholder, next_button_new = about_dependent_page(driver)
    email_elem.send_keys(new_user_email)
    phone_number_elem.send_keys(phone_number)
    street_address_elem.send_keys(street_address)
    city_elem.send_keys(city)
    state_elem.send_keys(Keys.UP, Keys.ENTER)
    next_button_new.click()

    first_name_elem_caregiver = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'caregiverFirstName')))
    last_name_elem_caregiver = driver.find_element(By.ID, 'caregiverLastName')
    email_elem_caregiver = driver.find_element(By.ID, 'caregiverEmail')
    phone_number_elem_caregiver = driver.find_element(By.ID, 'caregiverPhoneNumber')

    first_name_elem_caregiver_placeholder = driver.find_element(By.ID, 'caregiverFirstName-label')
    last_name_elem_caregiver_placeholder = driver.find_element(By.ID, 'caregiverLastName-label')
    email_elem_caregiver_placeholder = driver.find_element(By.ID, 'caregiverEmail-label')
    phone_number_elem_caregiver_placeholder = driver.find_element(By.ID, 'caregiverPhoneNumber-label')

    checkbox_elements = driver.find_elements(By.CLASS_NAME, 'sc-jxOSlx.gDdgcU')
    acknowledge_checkbox_elem = checkbox_elements[0]
    terms_privacy_elem = checkbox_elements[1]
    privacy_policy_link = driver.find_element(By.XPATH, '//a[@class="sc-tagGq ivXcxM" and contains(text(), "Privacy Policy")]')
    next_button_caregiver = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    terms_link = driver.find_element(By.XPATH, '//a[@class="sc-kdBSHD fGMyTe" and contains(text(), "Terms")]')
    privacy_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="sc-tagGq ivXcxM" and contains(text(), "Privacy Policy")]')))

    return privacy_policy_link, privacy_link, terms_link, first_name_elem_caregiver, last_name_elem_caregiver, email_elem_caregiver, phone_number_elem_caregiver, first_name_elem_caregiver_placeholder, last_name_elem_caregiver_placeholder, email_elem_caregiver_placeholder, phone_number_elem_caregiver_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, next_button_caregiver

