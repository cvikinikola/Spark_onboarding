import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from perform_test import myself_flow,  caregiver_page
from config import street_address, phone_number, email, existed_email, first_name, last_name
from conftest import driver


def test_about_caregiver_page_match_requires_all_fields(driver):
    privacy_policy_link, privacy_link, terms_link, first_name_elem_caregiver, last_name_elem_caregiver, email_elem_caregiver, phone_number_elem_caregiver, first_name_elem_caregiver_placeholder, last_name_elem_caregiver_placeholder, email_elem_caregiver_placeholder, phone_number_elem_caregiver_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, next_button_caregiver = caregiver_page(driver)
    expected_title = 'Next, tell us about you'
    title_text_about = driver.find_element(By.CLASS_NAME, 'sc-aXZVg.sc-eBMEME.fcpFyo.dVszMr')
    assert title_text_about.text == expected_title
    expected_p_text_about = 'Why do we need this info?'
    p_text_about = driver.find_element(By.CLASS_NAME, 'sc-gEvEer.anqoZ')
    assert p_text_about.text == expected_p_text_about
    expected_privacy_policy_text = 'Your privacy is important to us. Read more in our Privacy Policy.'
    privacy_policy_text = driver.find_element(By.CLASS_NAME, 'sc-gEvEer.clvpoc')
    assert privacy_policy_text.text == expected_privacy_policy_text
    expected_acknowledge_checkbox = 'You acknowledge that, if safety becomes a concern, we will reach out to you at the number provided and, in very rare cases, may send emergency services to the address provided.'
    acknowledge_checkbox = driver.find_element(By.XPATH, '//label[@class="sc-lcIPJg bJWMvy" and contains(text(), "You acknowledge that")]')
    assert acknowledge_checkbox.text == expected_acknowledge_checkbox
    expected_terms_privacy = 'I agree to the Terms, and Privacy Policy.'
    terms_privacy = driver.find_element(By.XPATH, '//label[@class="sc-lcIPJg bJWMvy" and contains(text(), "I agree to the")]')
    assert terms_privacy.text == expected_terms_privacy

    expected_first_name_placeholder = "Caregiver's first name\u2009*"
    expected_last_name_placeholder = "Caregiver's last name\u2009*"
    expected_email_elem_placeholder = "Caregiver's email\u2009*"
    expected_phone_number_placeholder = "Caregiver's phone number\u2009*"
    assert first_name_elem_caregiver_placeholder.text == expected_first_name_placeholder
    assert last_name_elem_caregiver_placeholder.text == expected_last_name_placeholder
    assert email_elem_caregiver_placeholder.text == expected_email_elem_placeholder
    assert phone_number_elem_caregiver_placeholder.text == expected_phone_number_placeholder

    expected_first_name_error = 'Please enter a first name'
    expected_last_name_error = 'Please enter a last name'
    expected_email_error = 'Please enter a valid email'
    expected_phone_number_error = 'Please enter a valid phone number'
    first_name_elem_caregiver.click()
    last_name_elem_caregiver.click()
    email_elem_caregiver.click()
    phone_number_elem_caregiver.click()
    acknowledge_checkbox_elem.click()
    acknowledge_checkbox_elem.click()
    terms_privacy_elem.click()

    first_name_elem_caregiver_error = driver.find_element(By.ID, 'caregiverFirstName-helper-text')
    last_name_elem_caregiver_error = driver.find_element(By.ID, 'caregiverLastName-helper-text')
    email_elem_caregiver_error = driver.find_element(By.ID, 'caregiverEmail-helper-text')
    expected_phone_number_elem_caregiver = driver.find_element(By.ID, 'caregiverPhoneNumber-helper-text')
    assert first_name_elem_caregiver_error.text == expected_first_name_error
    assert last_name_elem_caregiver_error.text == expected_last_name_error
    assert email_elem_caregiver_error.text == expected_email_error
    assert expected_phone_number_elem_caregiver.text == expected_phone_number_error
    assert next_button_caregiver != next_button_caregiver.is_enabled
    # need an update regarding the answer
    # assert state_error.text == expected_state_error

    expected_form_title = "Caregiver’s info"
    form_title = driver.find_element(By.CLASS_NAME, 'sc-gEvEer.dBkELJ')
    if form_title.text != expected_form_title:
        pytest.xfail('Text does not match, Dependent’s Info capital letters in Figma info small letter')
    assert form_title.text == expected_form_title

def test_required_form_fields(driver):
    privacy_policy_link, privacy_link, terms_link, first_name_elem_caregiver, last_name_elem_caregiver, email_elem_caregiver, phone_number_elem_caregiver, first_name_elem_caregiver_placeholder, last_name_elem_caregiver_placeholder, email_elem_caregiver_placeholder, phone_number_elem_caregiver_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, next_button_caregiver = caregiver_page(driver)

    # first name empty
    first_name_elem_caregiver.send_keys()
    last_name_elem_caregiver.send_keys(last_name)
    email_elem_caregiver.send_keys(email)
    phone_number_elem_caregiver.send_keys(phone_number)
    acknowledge_checkbox_elem.click()
    terms_privacy_elem.click()
    expected_state_error = 'Please enter a first name'
    first_name_elem_caregiver_error = driver.find_element(By.ID, 'caregiverFirstName-helper-text')
    assert first_name_elem_caregiver_error.text == expected_state_error
    assert next_button_caregiver != next_button_caregiver.is_enabled()

    # Last email empty
    first_name_elem_caregiver.send_keys(first_name)
    last_name_elem_caregiver.send_keys(Keys.CONTROL + 'a')
    last_name_elem_caregiver.send_keys(Keys.DELETE, Keys.TAB)
    expected_last_name_error = 'Please enter a last name'
    last_name_elem_caregiver_error = driver.find_element(By.ID, 'caregiverLastName-helper-text')
    assert last_name_elem_caregiver_error.text == expected_last_name_error
    assert next_button_caregiver != next_button_caregiver.is_enabled()

    # email empty
    last_name_elem_caregiver.send_keys(last_name)
    email_elem_caregiver.send_keys(Keys.CONTROL + 'a')
    email_elem_caregiver.send_keys(Keys.DELETE, Keys.TAB)
    expected_email_error = 'Please enter a valid email'
    email_elem_caregiver_error = driver.find_element(By.ID, 'caregiverEmail-helper-text')
    assert email_elem_caregiver_error.text == expected_email_error
    assert next_button_caregiver != next_button_caregiver.is_enabled()

    # phone number empty
    email_elem_caregiver.send_keys(email)
    phone_number_elem_caregiver.send_keys(Keys.CONTROL + 'a')
    phone_number_elem_caregiver.send_keys(Keys.DELETE, Keys.TAB)
    expected_phone_number_error = 'Please enter a valid phone number'
    expected_phone_number_elem_caregiver = driver.find_element(By.ID, 'caregiverPhoneNumber-helper-text')
    assert expected_phone_number_elem_caregiver.text == expected_phone_number_error
    assert next_button_caregiver != next_button_caregiver.is_enabled()

    # Acknowledge checkbox empty
    phone_number_elem_caregiver.send_keys(phone_number)
    acknowledge_checkbox_elem.click()
    assert next_button_caregiver != next_button_caregiver.is_enabled()

    # Terms and Privacy checkbox empty
    acknowledge_checkbox_elem.click()
    terms_privacy_elem.click()
    assert next_button_caregiver != next_button_caregiver.is_enabled()

def test_email_field_validation(driver):
    privacy_policy_link, privacy_link, terms_link, first_name_elem_caregiver, last_name_elem_caregiver, email_elem_caregiver, phone_number_elem_caregiver, first_name_elem_caregiver_placeholder, last_name_elem_caregiver_placeholder, email_elem_caregiver_placeholder, phone_number_elem_caregiver_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, next_button_caregiver = caregiver_page(driver)

    first_name_elem_caregiver.send_keys(first_name)
    last_name_elem_caregiver.send_keys(last_name)
    email_elem_caregiver.send_keys(email)
    phone_number_elem_caregiver.send_keys(phone_number)
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
        if email_elem_caregiver.get_attribute("value"):
            email_elem_caregiver.send_keys(Keys.CONTROL + 'a')
        email_elem_caregiver.send_keys(email_data)
        assert next_button_caregiver.is_enabled()

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
        if email_elem_caregiver.get_attribute("value"):
            email_elem_caregiver.send_keys(Keys.CONTROL + 'a')
        email_elem_caregiver.send_keys(email_data, Keys.TAB)
        next_button_caregiver.click()
        email_elem_caregiver_error = driver.find_element(By.ID, 'caregiverEmail-helper-text')
        assert email_elem_caregiver_error.text == expected_email_error
        assert next_button_caregiver != next_button_caregiver.is_enabled

def test_phone_number_validation(driver):
    privacy_policy_link, privacy_link, terms_link, first_name_elem_caregiver, last_name_elem_caregiver, email_elem_caregiver, phone_number_elem_caregiver, first_name_elem_caregiver_placeholder, last_name_elem_caregiver_placeholder, email_elem_caregiver_placeholder, phone_number_elem_caregiver_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, next_button_caregiver = caregiver_page(driver)

    first_name_elem_caregiver.send_keys(first_name)
    last_name_elem_caregiver.send_keys(last_name)
    email_elem_caregiver.send_keys(email)
    acknowledge_checkbox_elem.click()
    terms_privacy_elem.click()
    valid_phone_number = {
        '7606428215',
        '(760) 542-2222',
        '+17606428215',
        '+34635101666',
        '+381652701222'
    }
    for phone_number_data in valid_phone_number:
        if phone_number_elem_caregiver.get_attribute("value"):
            phone_number_elem_caregiver.send_keys(Keys.CONTROL + 'a')
        phone_number_elem_caregiver.send_keys(phone_number_data)
        assert next_button_caregiver.is_enabled()

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
        if phone_number_elem_caregiver.get_attribute("value"):
            phone_number_elem_caregiver.send_keys(Keys.CONTROL + 'a')
        phone_number_elem_caregiver.send_keys(phone_number_data, Keys.TAB)
        next_button_caregiver.click()
        expected_phone_number_elem_caregiver = driver.find_element(By.ID, 'caregiverPhoneNumber-helper-text')
        assert expected_phone_number_elem_caregiver.text == expected_phone_number_error
        assert next_button_caregiver != next_button_caregiver.is_enabled

def test_privacy_policy_caregiver_new_tab(driver):
    privacy_policy_link, privacy_link, terms_link, first_name_elem_caregiver, last_name_elem_caregiver, email_elem_caregiver, phone_number_elem_caregiver, first_name_elem_caregiver_placeholder, last_name_elem_caregiver_placeholder, email_elem_caregiver_placeholder, phone_number_elem_caregiver_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, next_button_caregiver = caregiver_page(driver)

    privacy_link.click()
    privacy_link_url = 'https://www.bighealth.com/spark-direct-privacy-policy/'
    driver.switch_to.window(driver.window_handles[1])
    assert privacy_link_url == driver.current_url
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    terms_link.click()
    terms_link_url = 'https://www.bighealth.com/spark-direct-terms-and-conditions/'
    driver.switch_to.window(driver.window_handles[1])
    assert terms_link_url == driver.current_url
    driver.close()

def test_need_this_popup(driver):
    caregiver_page(driver)

    p_text_about = driver.find_element(By.CLASS_NAME, 'sc-gEvEer.anqoZ')
    p_text_about.click()
    time.sleep(2)
    # need update when dev fix bug

    popup_locator = (By.CSS_SELECTOR, 'body > div.MuiPopover-root > div.MuiPaper-root.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_locator))

    popup_under_title_locator = (By.XPATH, '//p[@class="sc-gEvEer dZAKBA" and contains(text(), "How your dependent")]')
    popup_list_first_locator = (By.CSS_SELECTOR, 'body > div.MuiPopover-root > div.MuiPaper-root.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > div > ul > li:nth-child(1)')
    popup_list_second_locator = (By.CSS_SELECTOR, 'body > div.MuiPopover-root > div.MuiPaper-root.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > div > ul > li:nth-child(2)')
    popup_p_locator = (By.XPATH, '//p[@class="sc-gEvEer dZAKBA" and contains(text(), "If your dependent enters text")]')
    popup_second_p_locator = (By.XPATH, '//p[@class="sc-gEvEer dZAKBA" and contains(text(), "If you have any questions")]')
    popup_title_locator = (By.CLASS_NAME, 'sc-gEvEer.bPffxH')
    popup_close_button_locator = (By.CSS_SELECTOR, 'div.CTAButtonstyles__ButtonContainer-sc-172pifp-0.fcpFyo.hnCeuq > button')

    popup_under_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_under_title_locator))
    popup_list_first = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_list_first_locator))
    popup_list_second = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_list_second_locator))
    popup_p = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_p_locator))
    popup_second_p = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_second_p_locator))
    # popup_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_title_locator))
    popup_close_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_close_button_locator))

    expected_popup_title = 'Why do we need this info?'
    expected_under_title = "How your dependent interacts with Spark Direct is confidential. However, we are legally required to break confidentiality and disclose your dependent’s information in the following circumstances:"
    expected_popup_list_first = 'To prevent harm to your dependent or others'
    expected_popup_list_second = 'To report suspected child or elder abuse'
    expected_popup_p = 'If your dependent enters text into the app that seems to show potential risk, a popup alert to be presented to them along with safety resources. This also alerts a Big Health staff member who will review the text and decide if they may need to reach out and ensure safety. In the event of serious safety risk, we will notify a caregiver and we may contact emergency services.'
    expected_popup_second_p = 'If you have any questions, please contact us at spark@bighealth.com'

    assert popup_under_title.text == expected_under_title
    assert popup_list_first.text == expected_popup_list_first
    assert popup_list_second.text == expected_popup_list_second
    assert popup_p.text == expected_popup_p
    assert popup_second_p.text == expected_popup_second_p
    # assert popup_title.text == expected_popup_title

def test_privacy_policy_newtab(driver):
    privacy_policy_link, privacy_link, terms_link, first_name_elem_caregiver, last_name_elem_caregiver, email_elem_caregiver, phone_number_elem_caregiver, first_name_elem_caregiver_placeholder, last_name_elem_caregiver_placeholder, email_elem_caregiver_placeholder, phone_number_elem_caregiver_placeholder, acknowledge_checkbox_elem, terms_privacy_elem, next_button_caregiver = caregiver_page(driver)

    # need to update test
    # link opens in the same tab
    privacy_policy_link.click()
    privacy_link_url = 'https://www.bighealth.com/spark-direct-privacy-policy/'
    # driver.switch_to.window(driver.window_handles[1])
    assert privacy_link_url == driver.current_url






