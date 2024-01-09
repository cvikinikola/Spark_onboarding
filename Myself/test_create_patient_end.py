import time
import pytest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from perform_test import myself_flow,  about_your_page
from config import street_address, city, state, phone_number, email, new_user_email

def test_new_user_validation(driver):
    email_elem, phone_number_elem, street_address_elem, city_elem, state_elem, email_elem_placeholder, phone_number_placeholder, street_address_placeholder, city_placeholder, state_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, privacy_policy_link, next_button_new, terms_link, privacy_link = about_your_page(driver)

    email_elem.send_keys(new_user_email)
    phone_number_elem.send_keys(phone_number)
    street_address_elem.send_keys(street_address)
    city_elem.send_keys(city)
    state_elem.send_keys(Keys.UP, Keys.ENTER)
    acknowledge_checkbox_elem.click()
    terms_privacy_elem.click()
    next_button_new.click()

    what_page_next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")))
    what_page_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-eBMEME.fcpFyo.dVszMr')
    what_page_under_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-dCFHLb.fcpFyo.ctYaUb')
    expected_what_page_title = 'What’s next'
    expected_what_page_under_title = 'When you hit submit below, an app download link will be sent to you via text message.'
    assert what_page_title.text == expected_what_page_title
    assert what_page_under_title.text == expected_what_page_under_title
    what_page_next_button.click()

    time.sleep(1)
    download_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'CTAButtonstyles__Button')]")))
    last_page_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-eBMEME.fcpFyo.dVszMr')
    last_page_under_title = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-dCFHLb.fcpFyo.ctYaUb')
    last_page_first_p = driver.find_element(By.CLASS_NAME, 'sc-gEvEer.xCSRO')
    last_page_second_p = driver.find_element(By.CLASS_NAME, 'sc-gEvEer.crWrpR')

    expected_last_page_title = 'Text message sent!'
    expected_last_page_under_title = 'Please check your text message and download the app.'
    expected_last_page_first_p = 'Additional resources'
    expected_last_page_second_p = 'Want more information on how to navigate a mental health emergency? Feel free to download our resource below.'
    assert last_page_title.text == expected_last_page_title
    assert last_page_under_title.text == expected_last_page_under_title
    assert last_page_first_p.text == expected_last_page_first_p
    assert last_page_second_p.text == expected_last_page_second_p
    assert download_button.is_enabled()




