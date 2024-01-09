import time
import pytest

from perform_test import myself_flow,  dependent_sorry_page
from conftest import driver

def test_sorry_page(driver):
    we_are_sorry_page_title, first_under_title, second_under_title, experiencing_title, experiencing_first_p, experiencing_second_p, experiencing_third_p, suicide_title, suicide_p, crisis_text_title, crisis_text_p, LGBTQ_title, LGBTQ_p, suicide_link, LGBTQ_link, poison_control_title, poison_control_p, need_support_title, need_support_p, need_support_link, need_support_p_2, need_support_link_2, need_support_p_3, need_support_link_3, need_support_p_4 = dependent_sorry_page(driver)

    expected_we_are_sorry_page_title = "We’re sorry!"
    assert we_are_sorry_page_title.text == expected_we_are_sorry_page_title

    expected_first_under_title = "Your dependent is not eligible for Spark Direct through your insurance or employer."
    assert first_under_title.text == expected_first_under_title

    expected_second_under_title = "If you have any questions or need technical support, please contact us at spark@bighealth.com"
    assert second_under_title.text == expected_second_under_title

    expected_experiencing_title = "Experiencing a mental health emergency?"
    assert experiencing_title.text == expected_experiencing_title

    expected_experiencing_first_p = "If you are currently experiencing a mental health emergency or are having thoughts of self harm or suicide, please call 911 or go to the nearest emergency room."
    assert experiencing_first_p.text == expected_experiencing_first_p

    expected_experiencing_second_p = 'You can also call or text 988, a 24/7 suicide and crisis lifeline. They will connect you to a trained crisis worker who can help you find support right away.'
    assert experiencing_second_p.text == expected_experiencing_second_p

    expected_experiencing_third_p = 'If you are not in immediate danger but would like additional help, you can call or text a trained crisis worker who can give you immediate support. The services below are free and available 24/7, unless noted otherwise:'
    assert experiencing_third_p.text == expected_experiencing_third_p

    expected_suicide_title = "988 Suicide and Crisis Lifeline (includes self-harm):"
    assert suicide_title.text == expected_suicide_title

    expected_suicide_p = """Call 988\nChat online here."""
    assert suicide_p.text == expected_suicide_p

    # expected_suicide_second_p = 'For deaf or hard of hearing ASL users, call 988 Videophone.'
    # assert suicide_second_p == expected_suicide_second_p

    suicide_link.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    suicide_link_url = 'https://988lifeline.org/chat/'
    assert suicide_link_url == driver.current_url
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    expected_crisis_text_title = "Crisis Text Line:"
    assert crisis_text_title.text == expected_crisis_text_title

    expected_crisis_text_p = "Text HOME to 741741"
    assert crisis_text_p.text == expected_crisis_text_p

    expected_LGBTQ_title = "The Trevor Project (for LGBTQ youth):"
    assert LGBTQ_title.text == expected_LGBTQ_title

    expected_LGBTQ_title = """Call 1-866-488-7386\nText START to 678-678\nChat online here."""
    assert LGBTQ_p.text == expected_LGBTQ_title

    LGBTQ_link.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    LGBTQ_link_url = 'https://www.thetrevorproject.org/get-help/'
    assert LGBTQ_link_url == driver.current_url
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    expected_poison_control_title = "Poison Control:"
    assert poison_control_title.text == expected_poison_control_title

    expected_poison_control_p = "Call 1-800-222-1222"
    assert poison_control_p.text == expected_poison_control_p

    expected_need_support_title = "If you need support, but aren’t currently in a crisis:"
    assert need_support_title.text == expected_need_support_title

    expected_need_support_p = "This website can help you connect with in-person or long-term mental health care centers. It is both confidential and anonymous."
    assert need_support_p.text == expected_need_support_p

    expected_need_support_p_2 = "NAFC can help you find free and low-cost clinics in your community if you don’t have health insurance."
    assert need_support_p_2.text == expected_need_support_p_2

    expected_need_support_p_3 = """This site can connect you to low-cost social care providers to help you meet your mental health care needs.\nFilter by Health -> Mental Health Care."""
    assert need_support_p_3.text == expected_need_support_p_3

    expected_need_support_link = "Behavioral Health Treatment Services Locator:"
    assert need_support_link.text == expected_need_support_link
    need_support_link.click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    need_support_link_url = 'https://findtreatment.gov/'
    assert need_support_link_url == driver.current_url
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    expected_need_support_link_2 = "National Association of Free and Charitable Clinics:"
    assert need_support_link_2.text == expected_need_support_link_2
    need_support_link_2.click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    need_support_link_url_2 = 'https://nafcclinics.org/find-clinic/'
    assert need_support_link_url_2 == driver.current_url
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    expected_need_support_link_3 = "FindHelp:"
    assert need_support_link_3.text == expected_need_support_link_3
    need_support_link_3.click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    need_support_link_url_3 = 'https://www.findhelp.org/'
    assert need_support_link_url_3 == driver.current_url
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    expected_need_support_p_4 = "Big Health is not responsible for any actions or inactions between you and any third-party service provider. You acknowledge and agree that Big Health is not responsible for and expressly disclaims all liability for the actions or inactions of any third-party service provider."
    assert need_support_p_4.text == expected_need_support_p_4

