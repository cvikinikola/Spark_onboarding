import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from perform_test import dependent_flow
from config import (first_name, first_name_space, first_name_second_user, first_name_capital_letters, last_name_capital_letters, last_name, last_name_space, last_name_second_user, zip_code, zip_code_space, zip_code_invalid, employee_id_small_letter, employee_id, employee_id_space, employee_id_second_user, date_of_birth, date_of_birth_failed, date_of_birth_second_eser, date_of_birth_second_eser_failed, date_of_birth_not_eligible,first_name_under18, last_name_under18, date_of_birth_under18, employee_id_under18, zip_code_under18, first_name_under13, last_name_under13, date_of_birth_under13, employee_id_under13, zip_code_under13)
from conftest import driver

def test_dependent_not_eligible(driver):
    first_name_elem, last_name_elem, zip_code_elem, employee_id_elem, date_of_birth_elem, first_name_label, last_name_label, zip_code_label, employee_id_label, date_of_birth_label, check_coverage_button_elem = dependent_flow(driver)

    # Need update test when implemented feature
    first_name_elem.send_keys(first_name_space)
    last_name_elem.send_keys(last_name)
    zip_code_elem.send_keys(zip_code)
    employee_id_elem.send_keys(employee_id)
    date_of_birth_elem.send_keys(date_of_birth)
    check_coverage_button_elem.click()
    we_are_sorry_page_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-aXZVg.sc-esYiGF.fcpFyo.HOcMb')))
    expected_we_are_sorry_page_title = "We’re sorry!"
    assert we_are_sorry_page_title.text == expected_we_are_sorry_page_title

    # name + space
    # wait = WebDriverWait(driver, 10)
    # alert = wait.until(EC.alert_is_present())
    # alert_text = alert.text
    # expected_alert_text = """ApolloError: ["Employee details do not match what's on file"]"""
    # assert alert_text == expected_alert_text
    # alert.accept()

    # Last name + space
    driver.set_window_size(800, 800)
    back_arrow_elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.sc-gmPhUn.fcpFyo.eDRZGN > div > div.sc-aXZVg.sc-hRJfrW.fcpFyo.loHkfj > svg')))
    back_arrow_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    check_coverage_button_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    first_name_elem = driver.find_element(By.ID, 'coverageFormFirstName')
    last_name_elem = driver.find_element(By.ID, 'coverageFormLastName')
    first_name_elem.send_keys(Keys.CONTROL + 'a')
    first_name_elem.send_keys(first_name)
    last_name_elem.send_keys(Keys.CONTROL + 'a')
    last_name_elem.send_keys(last_name_space)
    check_coverage_button_elem.click()
    we_are_sorry_page_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-aXZVg.sc-esYiGF.fcpFyo.HOcMb')))
    assert we_are_sorry_page_title.text == expected_we_are_sorry_page_title


    # employee ID + space
    back_arrow_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    check_coverage_button_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    last_name_elem = driver.find_element(By.ID, 'coverageFormLastName')
    employee_id_elem = driver.find_element(By.ID, 'coverageFormEmployeeId')
    last_name_elem.send_keys(Keys.CONTROL + 'a')
    last_name_elem.send_keys(last_name)
    employee_id_elem.send_keys(Keys.CONTROL + 'a')
    employee_id_elem.send_keys(employee_id_space)
    check_coverage_button_elem.click()
    we_are_sorry_page_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-aXZVg.sc-esYiGF.fcpFyo.HOcMb')))
    assert we_are_sorry_page_title.text == expected_we_are_sorry_page_title

    # non eligible date
    back_arrow_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    check_coverage_button_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    employee_id_elem = driver.find_element(By.ID, 'coverageFormEmployeeId')
    date_of_birth_elem = driver.find_element(By.ID, 'coverageFormDOB')
    employee_id_elem.send_keys(Keys.CONTROL + 'a')
    employee_id_elem.send_keys(employee_id)
    date_of_birth_elem.send_keys(Keys.CONTROL + 'a')
    date_of_birth_elem.send_keys(date_of_birth_not_eligible)
    check_coverage_button_elem.click()
    we_are_sorry_page_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-aXZVg.sc-esYiGF.fcpFyo.HOcMb')))
    assert we_are_sorry_page_title.text == expected_we_are_sorry_page_title

    # eligible date of second user
    back_arrow_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    check_coverage_button_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    date_of_birth_elem = driver.find_element(By.ID, 'coverageFormDOB')
    date_of_birth_elem.send_keys(Keys.CONTROL + 'a')
    date_of_birth_elem.send_keys(date_of_birth_second_eser)
    check_coverage_button_elem.click()
    we_are_sorry_page_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-aXZVg.sc-esYiGF.fcpFyo.HOcMb')))
    assert we_are_sorry_page_title.text == expected_we_are_sorry_page_title

    # eligible Employee ID of second user
    back_arrow_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    check_coverage_button_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    date_of_birth_elem = driver.find_element(By.ID, 'coverageFormDOB')
    employee_id_elem = driver.find_element(By.ID, 'coverageFormEmployeeId')
    date_of_birth_elem.send_keys(Keys.CONTROL + 'a')
    date_of_birth_elem.send_keys(date_of_birth)
    employee_id_elem.send_keys(Keys.CONTROL + 'a')
    employee_id_elem.send_keys(employee_id_second_user)
    check_coverage_button_elem.click()
    we_are_sorry_page_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-aXZVg.sc-esYiGF.fcpFyo.HOcMb')))
    assert we_are_sorry_page_title.text == expected_we_are_sorry_page_title

    # eligible First name of second user
    back_arrow_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    check_coverage_button_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    first_name_elem = driver.find_element(By.ID, 'coverageFormFirstName')
    employee_id_elem = driver.find_element(By.ID, 'coverageFormEmployeeId')
    employee_id_elem.send_keys(Keys.CONTROL + 'a')
    employee_id_elem.send_keys(employee_id)
    first_name_elem.send_keys(Keys.CONTROL + 'a')
    first_name_elem.send_keys(first_name_second_user)
    check_coverage_button_elem.click()
    we_are_sorry_page_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-aXZVg.sc-esYiGF.fcpFyo.HOcMb')))
    assert we_are_sorry_page_title.text == expected_we_are_sorry_page_title

    # eligible Last name of second user
    back_arrow_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    check_coverage_button_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    first_name_elem = driver.find_element(By.ID, 'coverageFormFirstName')
    last_name_elem = driver.find_element(By.ID, 'coverageFormLastName')
    first_name_elem.send_keys(Keys.CONTROL + 'a')
    first_name_elem.send_keys(first_name)
    last_name_elem.send_keys(Keys.CONTROL + 'a')
    last_name_elem.send_keys(last_name_second_user)
    check_coverage_button_elem.click()
    we_are_sorry_page_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-aXZVg.sc-esYiGF.fcpFyo.HOcMb')))
    assert we_are_sorry_page_title.text == expected_we_are_sorry_page_title

    # need to update regarding the answer
    # zip code is not eligible but user can pass form
    back_arrow_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    check_coverage_button_elem.click()
    check_coverage_button_elem = driver.find_element(By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")
    last_name_elem = driver.find_element(By.ID, 'coverageFormLastName')
    zip_code_elem = driver.find_element(By.ID, 'coverageFormZipCode')
    last_name_elem.send_keys(Keys.CONTROL + 'a')
    last_name_elem.send_keys(last_name)
    zip_code_elem.send_keys(Keys.CONTROL + 'a')
    zip_code_elem.send_keys(zip_code_invalid)
    check_coverage_button_elem.click()
    # we_are_sorry_page_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-aXZVg.sc-esYiGF.fcpFyo.HOcMb')))
    # assert we_are_sorry_page_title.text == expected_we_are_sorry_page_title
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")))
    you_are_covered_page_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-eBMEME.fcpFyo.dVszMr')
    expected_you_are_covered_page_title = "Your dependent is covered!"
    assert you_are_covered_page_title.text == expected_you_are_covered_page_title

def test_dependent_eligible(driver):
    first_name_elem, last_name_elem, zip_code_elem, employee_id_elem, date_of_birth_elem, first_name_label, last_name_label, zip_code_label, employee_id_label, date_of_birth_label, check_coverage_button_elem = dependent_flow(driver)
    first_name_elem.send_keys(first_name_capital_letters)
    last_name_elem.send_keys(last_name_capital_letters)
    zip_code_elem.send_keys(zip_code)
    employee_id_elem.send_keys(employee_id_small_letter)
    date_of_birth_elem.send_keys(date_of_birth)
    check_coverage_button_elem.click()
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")))
    you_are_covered_page_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-eBMEME.fcpFyo.dVszMr')
    expected_you_are_covered_page_title = "Your dependent is covered!"
    assert you_are_covered_page_title.text == expected_you_are_covered_page_title

def test_dependent_eligible_under_13(driver):
    first_name_elem, last_name_elem, zip_code_elem, employee_id_elem, date_of_birth_elem, first_name_label, last_name_label, zip_code_label, employee_id_label, date_of_birth_label, check_coverage_button_elem = dependent_flow(driver)
    # Need update test when implemented feature
    first_name_elem.send_keys(first_name_under13)
    last_name_elem.send_keys(last_name_under13)
    zip_code_elem.send_keys(zip_code_under13)
    employee_id_elem.send_keys(employee_id_under13)
    date_of_birth_elem.send_keys(date_of_birth_under13)
    check_coverage_button_elem.click()
    date_of_birth_error_under13 = driver.find_element(By.ID, 'coverageFormDOB-helper-text')
    expected_date_of_birth_error_under13 = 'Spark Direct is not intended for users under the age of 13. If your dependent is under the age of 13, they are not eligible to use Spark Direct.'
    assert date_of_birth_error_under13.text == expected_date_of_birth_error_under13
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    expected_alert_text = """ApolloError: ['Spark Direct is not intended for users under the age of 13']"""
    assert alert_text == expected_alert_text
    alert.accept()

def test_dependent_eligible_under_18(driver):
    first_name_elem, last_name_elem, zip_code_elem, employee_id_elem, date_of_birth_elem, first_name_label, last_name_label, zip_code_label, employee_id_label, date_of_birth_label, check_coverage_button_elem = dependent_flow(driver)
    first_name_elem.send_keys(first_name_under18)
    last_name_elem.send_keys(last_name_under18)
    zip_code_elem.send_keys(zip_code_under18)
    employee_id_elem.send_keys(employee_id_under18)
    date_of_birth_elem.send_keys(date_of_birth_under18)
    check_coverage_button_elem.click()
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")))
    you_are_covered_page_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-eBMEME.fcpFyo.dVszMr')
    expected_you_are_covered_page_title = "Your dependent is covered!"
    assert you_are_covered_page_title.text == expected_you_are_covered_page_title