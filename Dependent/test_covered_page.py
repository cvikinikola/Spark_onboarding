import pytest

from perform_test import myself_flow,  covered_page_dependent
from conftest import driver

def test_covered_page_match(driver):
    next_button_coverage, you_are_covered_page_title, you_are_covered_page_p, you_are_covered_page_what, you_are_covered_page_answer, you_are_covered_page_download, you_are_covered_page_start = covered_page_dependent(driver)
    expected_you_are_covered_page_title = "Your dependent is covered!"
    assert you_are_covered_page_title.text == expected_you_are_covered_page_title

    expected_you_are_covered_page_p = 'Thanks for taking the first step in helping your dependent receive care with Spark Direct.'
    assert you_are_covered_page_p.text == expected_you_are_covered_page_p

    expected_you_are_covered_page_what = "What's next:"
    assert you_are_covered_page_what.text == expected_you_are_covered_page_what

    expected_you_are_covered_page_answer = 'You will answer several questions'
    assert you_are_covered_page_answer.text == expected_you_are_covered_page_answer

    expected_you_are_covered_page_download = 'Your dependent will download the Spark Direct app'
    assert you_are_covered_page_download.text == expected_you_are_covered_page_download

    expected_you_are_covered_page_start = 'They can start seeing benefits of Spark Direct'
    assert you_are_covered_page_start.text == expected_you_are_covered_page_start