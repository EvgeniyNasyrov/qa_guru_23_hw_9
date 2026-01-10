# tests/test_registration.py
import pytest
from selene import browser
from Part_1.page_objects.registration_page import RegistrationPage


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.timeout = 6
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


def test_automation_practice_form():
    registration_page = RegistrationPage()

    registration_page.open() \
        .fill_first_name('Evgeniy') \
        .fill_last_name('Student') \
        .fill_user_email('Stud_Evg@example.com') \
        .select_gender('1') \
        .fill_phone_number('9321217654') \
        .set_birth_date(2000, 'June', 15) \
        .fill_subjects('English') \
        .select_hobby(1) \
        .upload_picture('test.jpg') \
        .fill_address('Moscow, Russia') \
        .select_state('NCR') \
        .select_city('Delhi') \
        .submit() \
        .should_have_registered(
            first_name='Evgeniy',
            last_name='Student',
            email='Stud_Evg@example.com',
            phone_number='9321217654',
            birth_date='15 June,2000',
            subject='English',
            hobby='Sports',
            address='Moscow, Russia',
            state_and_city='NCR Delhi'
        )