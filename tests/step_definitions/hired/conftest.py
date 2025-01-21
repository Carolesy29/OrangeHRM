import pytest
from pytest_bdd import given, parsers

from tests import FlowHired

CREATE_CANDIDATE = FlowHired()


@pytest.fixture(scope="class", autouse=True)
def tests_setup_and_teardown():
    yield
    CREATE_CANDIDATE.quit_page()


@given(parsers.parse("that the page is opened for a in {browser} device"))
def open_login_page(browser):
    CREATE_CANDIDATE.open_page(browser)
