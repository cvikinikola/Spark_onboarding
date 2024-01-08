
from perform_test import setup_driver, myself_flow,  covered_page


def test_covered_page_match():
    driver = setup_driver()
    next_button_coverage, you_are_covered_page_title, you_are_covered_page_p, you_are_covered_page_what, you_are_covered_page_answer, you_are_covered_page_download, you_are_covered_page_start = covered_page(driver)
    expected_you_are_covered_page_title = "You're covered!"
    assert you_are_covered_page_title.text == expected_you_are_covered_page_title

    expected_you_are_covered_page_p = 'Thanks for taking the first step in your treatment journey with Spark Direct.'
    assert you_are_covered_page_p.text == expected_you_are_covered_page_p

    expected_you_are_covered_page_what = "What's next:"
    assert you_are_covered_page_what.text == expected_you_are_covered_page_what

    expected_you_are_covered_page_answer = 'Answer several questions'
    assert you_are_covered_page_answer.text == expected_you_are_covered_page_answer

    expected_you_are_covered_page_download = 'Download the Spark Direct app'
    assert you_are_covered_page_download.text == expected_you_are_covered_page_download

    expected_you_are_covered_page_start = 'Start seeing the benefits of Spark Direct'
    assert you_are_covered_page_start.text == expected_you_are_covered_page_start




