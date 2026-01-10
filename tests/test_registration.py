# tests/test_registration.py
import pytest
from selene import browser
from page_objects.registration_page import RegistrationPage
from models.user import student


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.timeout = 6
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


def test_automation_practice_form():
    page = RegistrationPage()
    page.open()
    page.register(student)
    page.should_have_registered(student)