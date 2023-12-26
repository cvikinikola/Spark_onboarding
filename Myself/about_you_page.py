import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from perform_test import setup_driver, perform_test,  about_your_page
from config import street_address, city, state, phone_number, email


def test_about_your_page_match_requires_all_fields():
    driver = setup_driver()
    email_elem, phone_number_elem, street_address_elem, city_elem, state_elem, email_elem_placeholder, phone_number_placeholder, street_address_placeholder, city_placeholder, state_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, privacy_policy_link, next_button_new, terms_link, privacy_link = about_your_page(driver)
    expected_p_text_about = 'Why do we need this info?'
    p_text_about = driver.find_element(By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.PatientInfostyles__HoverContainer-sc-y7jovp-0.bbGRJy')
    assert p_text_about.text == expected_p_text_about
    expected_privacy_policy_text = 'Your privacy is important to us. Read more in our Privacy Policy.'
    privacy_policy_text = driver.find_element(By.CLASS_NAME, 'sc-gEvEer.clvpoc')
    assert privacy_policy_text.text == expected_privacy_policy_text
    expected_acknowledge_checkbox = 'You acknowledge that, if safety becomes a concern, we will reach out to you at the number provided and, in very rare cases, may send emergency services to the address provided.'
    acknowledge_checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(10) > label')))
    assert acknowledge_checkbox.text == expected_acknowledge_checkbox
    expected_terms_privacy = 'I agree to the Terms, and Privacy Policy.'
    terms_privacy = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div:nth-child(11) > label')))
    assert terms_privacy.text == expected_terms_privacy

    expected_email_error = 'Please enter a valid email'
    expected_phone_number_error = 'Please enter a valid phone number'
    expected_street_error = 'Please enter a valid address'
    expected_city_error = 'Please enter a valid city'
    # need an update regarding the answer
    # expected_state_error = 'Please enter a valid state'
    email_elem.click()
    phone_number_elem.click()
    street_address_elem.click()
    city_elem.click()
    state_elem.send_keys(Keys.TAB)
    acknowledge_checkbox_elem.click()
    terms_privacy_elem.click()
    email_error = driver.find_element(By.ID, 'patientEmail-helper-text')
    phone_number_error = driver.find_element(By.ID, 'patientPhoneNumber-helper-text')
    street_error = driver.find_element(By.ID, 'patientStreetAddress-helper-text')
    city_error = driver.find_element(By.ID, 'patientCity-helper-text')
    # state_error = driver.find_element(By.ID, 'patientState-helper-text')
    assert email_error.text == expected_email_error
    assert phone_number_error.text == expected_phone_number_error
    assert street_error.text == expected_street_error
    assert city_error.text == expected_city_error
    # need an update regarding the answer
    # assert state_error.text == expected_state_error

    expected_title = "Next, tell us about you"
    title_text_about = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.sc-aXZVg.sc-eBMEME.fcpFyo.dVszMr')))
    if title_text_about.text != expected_title:
        pytest.xfail('Text does not match, reported and received a reply that it is not a bug')
    assert title_text_about.text == expected_title

    expected_form_title = 'Your info'
    form_title = driver.find_element(By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > p')
    if form_title.text != expected_form_title:
        pytest.xfail('Text does not match, Your Info capital letters in Figma info small letter')
    assert form_title.text == expected_form_title


def test_required_form_fields():
    driver = setup_driver()
    email_elem, phone_number_elem, street_address_elem, city_elem, state_elem, email_elem_placeholder, phone_number_placeholder, street_address_placeholder, city_placeholder, state_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, privacy_policy_link, next_button_new, terms_link, privacy_link = about_your_page(driver)

    # State empty
    email_elem.send_keys(email)
    phone_number_elem.send_keys(phone_number)
    street_address_elem.send_keys(street_address)
    city_elem.send_keys(city)
    acknowledge_checkbox_elem.click()
    terms_privacy_elem.click()
    # expected_state_error = 'Please enter a valid state'
    # state_error = driver.find_element(By.ID, 'patientState-helper-text')
    # assert state_error.text == expected_state_error
    assert next_button_new != next_button_new.is_enabled()

    # Email empty
    email_elem.send_keys(Keys.CONTROL + 'a')
    email_elem.send_keys(Keys.DELETE, Keys.TAB)
    state_elem.send_keys(Keys.UP, Keys.ENTER)
    expected_email_error = 'Please enter a valid email'
    email_error = driver.find_element(By.ID, 'patientEmail-helper-text')
    assert email_error.text == expected_email_error
    assert next_button_new != next_button_new.is_enabled()

    # Phone number empty
    email_elem.send_keys(email)
    phone_number_elem.send_keys(Keys.CONTROL + 'a')
    phone_number_elem.send_keys(Keys.DELETE, Keys.TAB)
    expected_phone_number_error = 'Please enter a valid phone number'
    phone_number_error = driver.find_element(By.ID, 'patientPhoneNumber-helper-text')
    assert phone_number_error.text == expected_phone_number_error
    assert next_button_new != next_button_new.is_enabled()

    # Street address empty
    phone_number_elem.send_keys(phone_number)
    street_address_elem.send_keys(Keys.CONTROL + 'a')
    street_address_elem.send_keys(Keys.DELETE, Keys.TAB)
    expected_street_error = 'Please enter a valid address'
    street_error = driver.find_element(By.ID, 'patientStreetAddress-helper-text')
    assert street_error.text == expected_street_error
    assert next_button_new != next_button_new.is_enabled()

    # City empty
    street_address_elem.send_keys(street_address)
    city_elem.send_keys(Keys.CONTROL + 'a')
    city_elem.send_keys(Keys.DELETE, Keys.TAB)
    expected_city_error = 'Please enter a valid city'
    city_error = driver.find_element(By.ID, 'patientCity-helper-text')
    assert city_error.text == expected_city_error
    assert next_button_new != next_button_new.is_enabled()

    # Acknowledge checkbox empty
    city_elem.send_keys(city)
    acknowledge_checkbox_elem.click()
    assert next_button_new != next_button_new.is_enabled()

    # Terms and Privacy checkbox empty
    acknowledge_checkbox_elem.click()
    terms_privacy_elem.click()
    assert next_button_new != next_button_new.is_enabled()


def test_email_field_validation():
    driver = setup_driver()
    email_elem, phone_number_elem, street_address_elem, city_elem, state_elem, email_elem_placeholder, phone_number_placeholder, street_address_placeholder, city_placeholder, state_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, privacy_policy_link, next_button_new, terms_link, privacy_link = about_your_page(driver)

    phone_number_elem.send_keys(phone_number)
    street_address_elem.send_keys(street_address)
    city_elem.send_keys(city)
    state_elem.send_keys(Keys.UP, Keys.ENTER)
    acknowledge_checkbox_elem.click()
    terms_privacy_elem.click()

    valid_email = {
        'email@example.name',
        '_______@example.com',
        'email@example-one.com',
        '1234567890@example.com',
        '"email"@example.com',
        'email@[123.123.123.123]',
        'email@123.123.123.123',
        'firstname+lastname@example.com',
        'email@subdomain.example.com',
        'firstname.lastname@example.com',
        'email@example.com',
        'email@example.co.jp',
        'email@example.museum'
    }
    for email_data in valid_email:
        if email_elem.get_attribute("value"):
            email_elem.send_keys(Keys.CONTROL + 'a')
        email_elem.send_keys(email_data)
        assert next_button_new.is_enabled()

    expected_email_error = 'Please enter a valid email'
    invalid_email = {
        'plainaddress',
        'this\ is"really"not\allowed@example.com',
        '❤️.efef@dsv.com',
        'email@example.com@@   @@@@  @@@example.com',
        '#@%^%#$@#$@#.com',
        '@example.com',
        'Joe Smith <email@example.com>',
        'email.example.com',
        'email@example@example.com',
        '.email@example.com',
        'email.@example.com',
        'email..email@example.com',
        'あいうえお@example.com',
        'email@example.com (Joe Smith)',
        'email@example',
        'email@-example.com',
        'email@example.web',
        'email@111.222.333.44444',
        'email@example..com',
        'Abc..123@example.com',
    }
    for email_data in invalid_email:
        if email_elem.get_attribute("value"):
            email_elem.send_keys(Keys.CONTROL + 'a')
        email_elem.send_keys(email_data, Keys.TAB)
        next_button_new.click()
        email_error = driver.find_element(By.ID, 'patientEmail-helper-text')
        assert email_error.text == expected_email_error
        assert next_button_new != next_button_new.is_enabled


def test_phone_number_validation():
    driver = setup_driver()
    email_elem, phone_number_elem, street_address_elem, city_elem, state_elem, email_elem_placeholder, phone_number_placeholder, street_address_placeholder, city_placeholder, state_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, privacy_policy_link, next_button_new, terms_link, privacy_link = about_your_page(driver)

    street_address_elem.send_keys(street_address)
    city_elem.send_keys(city)
    state_elem.send_keys(Keys.UP, Keys.ENTER)
    acknowledge_checkbox_elem.click()
    terms_privacy_elem.click()

    valid_phone_number = {
        '7606428215',
        '1 (760) 542-22',
        '+17606428215',
        '+34635101666',
        '+381652701222'
    }
    for phone_number_data in valid_phone_number:
        if phone_number_elem.get_attribute("value"):
            phone_number_elem.send_keys(Keys.CONTROL + 'a')
        phone_number_elem.send_keys(phone_number_data)
        assert next_button_new.is_enabled()

    expected_phone_number_error = 'Please enter a valid phone number'
    invalid_phone_number = {
        '123',
        'abc',
        '+',
        '+381',
        '+38165Æ',
        '12 34 56 78 90 12'
    }
    for phone_number_data in invalid_phone_number:
        if phone_number_elem.get_attribute("value"):
            phone_number_elem.send_keys(Keys.CONTROL + 'a')
        phone_number_elem.send_keys(phone_number_data, Keys.TAB)
        next_button_new.click()
        phone_number_error = driver.find_element(By.ID, 'patientPhoneNumber-helper-text')
        assert phone_number_error.text == expected_phone_number_error
        assert next_button_new != next_button_new.is_enabled

def test_privacy_policy_newtab():
    driver = setup_driver()
    email_elem, phone_number_elem, street_address_elem, city_elem, state_elem, email_elem_placeholder, phone_number_placeholder, street_address_placeholder, city_placeholder, state_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, privacy_policy_link, next_button_new, terms_link, privacy_link = about_your_page(driver)

    privacy_link.click()
    privacy_link_url = 'https://www.bighealth.com/spark-direct-privacy-policy/'
    driver.switch_to.window(driver.window_handles[2])
    assert privacy_link_url == driver.current_url
    driver.close()

    driver.switch_to.window(driver.window_handles[1])
    terms_link.click()
    terms_link_url = 'https://www.bighealth.com/spark-direct-terms-and-conditions/'
    driver.switch_to.window(driver.window_handles[2])
    assert terms_link_url == driver.current_url
    driver.close()

def test_need_this_popup():
    driver = setup_driver()
    email_elem, phone_number_elem, street_address_elem, city_elem, state_elem, email_elem_placeholder, phone_number_placeholder, street_address_placeholder, city_placeholder, state_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, privacy_policy_link, next_button_new, terms_link, privacy_link = about_your_page(driver)

    p_text_about = driver.find_element(By.CSS_SELECTOR, '#root > div > div.sc-aXZVg.OnboardingPagestyles__PageContentContainer-sc-7dyz4y-1.fcpFyo.ruVSJ > div > form > div.PatientInfostyles__HoverContainer-sc-y7jovp-0.bbGRJy')
    p_text_about.click()
    time.sleep(2)
    # need update when dev fix bug

    popup_locator = (By.CSS_SELECTOR, 'body > div.MuiPopover-root > div.MuiPaper-root.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_locator))

    popup_under_title_locator = (By.CSS_SELECTOR, 'body > div.MuiPopover-root > div.MuiPaper-root.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > div > div:nth-child(3) > p')
    popup_list_first_locator = (By.CSS_SELECTOR, 'body > div.MuiPopover-root > div.MuiPaper-root.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > div > ul > li:nth-child(1)')
    popup_list_second_locator = (By.CSS_SELECTOR, 'body > div.MuiPopover-root > div.MuiPaper-root.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > div > ul > li:nth-child(2)')
    popup_p_locator = (By.CSS_SELECTOR, 'body > div.MuiPopover-root > div.MuiPaper-root.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > div > div:nth-child(5) > p')
    popup_second_p_locator = (By.CSS_SELECTOR, 'body > div.MuiPopover-root > div.MuiPaper-root.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > div > div:nth-child(6) > p')
    popup_title_locator = (By.CSS_SELECTOR, 'div.OnboardingPopoverstyles__PopoverDesktopContainer-sc-gjairf-1.fcpFyo.ijzARy > p.bPffxH')
    popup_close_button_locator = (By.CSS_SELECTOR, 'div.CTAButtonstyles__ButtonContainer-sc-172pifp-0.fcpFyo.hnCeuq > button')

    popup_under_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_under_title_locator))
    popup_list_first = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_list_first_locator))
    popup_list_second = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_list_second_locator))
    popup_p = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_p_locator))
    popup_second_p = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_second_p_locator))
    # popup_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_title_locator))
    popup_close_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_close_button_locator))

    expected_popup_title = 'Why do we need this info?'
    expected_under_title = 'The text you enter and how you engage with Spark Direct is confidential and meant for only you. However, we are legally required to break confidentiality and disclose your information in the following circumstances:'
    expected_popup_list_first = 'To prevent harm to you or others'
    expected_popup_list_second = 'To report suspected child or elder abuse'
    expected_popup_p = 'If you enter text into Spark Direct that seems to show potential risk, a popup alert will be presented to you along with safety resources. A Big Health staff member will also be alerted, and they will review the text and decide if they need to reach out to ensure safety. In the event of serious safety risk, we may contact emergency services.'
    expected_popup_second_p = 'If you have any questions, please contact us at spark@bighealth.com'

    assert popup_under_title.text == expected_under_title
    assert popup_list_first.text == expected_popup_list_first
    assert popup_list_second.text == expected_popup_list_second
    assert popup_p.text == expected_popup_p
    assert popup_second_p.text == expected_popup_second_p
    # assert popup_title.text == expected_popup_title

def test_same_email_validation():
    driver = setup_driver()
    email_elem, phone_number_elem, street_address_elem, city_elem, state_elem, email_elem_placeholder, phone_number_placeholder, street_address_placeholder, city_placeholder, state_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, privacy_policy_link, next_button_new, terms_link, privacy_link = about_your_page(driver)

    # same email or existing email bug no validation
    email_elem.send_keys(email)
    phone_number_elem.send_keys(phone_number)
    street_address_elem.send_keys(street_address)
    city_elem.send_keys(city)
    state_elem.send_keys(Keys.UP, Keys.ENTER)
    acknowledge_checkbox_elem.click()
    terms_privacy_elem.click()
    next_button_new.click()
    expected_email_error = 'Please enter a valid email'
    email_error = driver.find_element(By.ID, 'patientEmail-helper-text')
    assert email_error.text == expected_email_error
    assert next_button_new != next_button_new.is_enabled()
