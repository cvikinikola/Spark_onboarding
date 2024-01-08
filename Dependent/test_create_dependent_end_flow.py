import time

from selenium.webdriver.common.keys import Keys
import os
import time
from selenium import webdriver

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from perform_test import setup_driver, myself_flow,  coregiver_page
from config import street_address, phone_number, email, existed_email, first_name, last_name

def test_new_dependent_validation():
    driver = setup_driver()
    privacy_policy_link, privacy_link, terms_link, first_name_elem_caregiver, last_name_elem_caregiver, email_elem_caregiver, phone_number_elem_caregiver, first_name_elem_caregiver_placeholder, last_name_elem_caregiver_placeholder, email_elem_caregiver_placeholder, phone_number_elem_caregiver_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, next_button_caregiver = coregiver_page(driver)

    first_name_elem_caregiver.send_keys(first_name)
    last_name_elem_caregiver.send_keys(last_name)
    email_elem_caregiver.send_keys(email)
    phone_number_elem_caregiver.send_keys(phone_number)
    acknowledge_checkbox_elem.click()
    terms_privacy_elem.click()
    next_button_caregiver.click()

    what_page_next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")))
    what_page_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-eBMEME.fcpFyo.dVszMr')
    what_page_under_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-dCFHLb.fcpFyo.ctYaUb')
    please_make_sure_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-Nxspf.fcpFyo.dVaKcL')
    first_subtitle = driver.find_element(By.XPATH, '//p[@class="sc-gEvEer fixEOS" and contains(text(), "Talk to your dependent")]')
    second_subtitle = driver.find_element(By.XPATH, '//p[@class="sc-gEvEer fixEOS" and contains(text(), "Dependent’s phone can receive text")]')
    third_subtitle = driver.find_element(By.XPATH, '//p[@class="sc-gEvEer fixEOS" and contains(text(), "Dependent has time to")]')
    # wrong Curly apostrophe / Straight apostrophe
    expected_what_page_title = "What's next"
    assert what_page_title.text == expected_what_page_title
    expected_what_page_under_title = 'When you hit submit below, an app download link will be sent to your dependent via text message.'
    assert what_page_under_title.text == expected_what_page_under_title
    expected_please_make_sure_title = "Please make sure"
    assert please_make_sure_title.text == expected_please_make_sure_title
    expected_first_subtitle = 'Talk to your dependent about Spark Direct'
    assert first_subtitle.text == expected_first_subtitle
    expected_second_subtitle = 'Dependent’s phone can receive text messages and use the Spark Direct app'
    assert second_subtitle.text == expected_second_subtitle
    expected_third_subtitle = 'Dependent has time to start Spark Direct'
    assert third_subtitle.text == expected_third_subtitle
    what_page_next_button.click()

    download_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")))
    last_page_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-eBMEME.fcpFyo.dVszMr')
    last_page_under_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-dCFHLb.fcpFyo.ctYaUb')
    last_page_first_p = driver.find_element(By.CLASS_NAME, 'sc-gEvEer.xCSRO')
    last_page_second_p = driver.find_element(By.CLASS_NAME, 'sc-gEvEer.crWrpR')

    expected_last_page_title = 'Text message sent!'
    expected_last_page_under_title = 'Please remind your dependent to use the text link to download and begin the program.'
    expected_last_page_first_p = 'Additional resources for caregivers'
    expected_last_page_second_p = 'We’ve created a guide for introducing Spark Direct to your dependent. The guide contains information on Spark Direct, how to communicate with young people with depression, as well as information about suicide and crisis resources.'
    assert last_page_title.text == expected_last_page_title
    assert last_page_under_title.text == expected_last_page_under_title
    assert last_page_first_p.text == expected_last_page_first_p
    assert last_page_second_p.text == expected_last_page_second_p
    assert download_button.is_enabled()