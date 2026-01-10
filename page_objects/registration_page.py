# page_objects/registration_page.py
from selene import browser, have, by
import os
from models.user import User


class RegistrationPage:
    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")
        return self

    def register(self, user: User):
        self._fill_first_name(user.first_name)
        self._fill_last_name(user.last_name)
        self._fill_email(user.email)
        self._select_gender("1")
        self._fill_phone(user.phone_number)
        self._set_birth_date(user.birth_date)
        self._fill_subjects(user.subjects)
        self._select_hobby(user.hobby)
        self._upload_picture(user.picture_file)
        self._fill_address(user.address)
        self._select_state_and_city(user.state, user.city)
        self._submit()
        return self

    def should_have_registered(self, user: User):
        modal = browser.element(".modal-body")
        modal.should(have.text(user.full_name))
        modal.should(have.text(user.email))
        modal.should(have.text(user.phone_number))
        modal.should(have.text(user.birth_date_str))
        for subject in user.subjects:
            modal.should(have.text(subject))
        modal.should(have.text(user.hobby.value))
        modal.should(have.text(user.picture_file))
        modal.should(have.text(user.address))
        modal.should(have.text(user.state_and_city))
        return self

    # --- Приватные методы ---
    def _fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def _fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def _fill_email(self, value):
        browser.element("#userEmail").type(value)

    def _select_gender(self, gender_id):
        browser.element(f'label[for="gender-radio-{gender_id}"]').click()

    def _fill_phone(self, value):
        browser.element("#userNumber").type(value)

    def _set_birth_date(self, birth_date):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").element(by.text(str(birth_date.year))).click()
        month_name = birth_date.strftime("%B")
        browser.element(".react-datepicker__month-select").element(by.text(month_name)).click()
        day = str(birth_date.day)
        browser.all(".react-datepicker__day:not(.react-datepicker__day--outside-month)").element_by(
            have.exact_text(day)
        ).click()

    def _fill_subjects(self, subjects):
        for subject in subjects:
            browser.element("#subjectsInput").type(subject).press_enter()

    def _select_hobby(self, hobby):
        mapping = {"Sports": 1, "Reading": 2, "Music": 3}
        hobby_id = mapping[hobby.value]
        browser.element(f'label[for="hobbies-checkbox-{hobby_id}"]').click()

    def _upload_picture(self, filename):
        current_dir = os.path.dirname(__file__)
        file_path = os.path.abspath(os.path.join(current_dir, "..", "tests", filename))
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        browser.element("#uploadPicture").send_keys(file_path)

    def _fill_address(self, value):
        browser.element("#currentAddress").type(value)

    def _select_state_and_city(self, state, city):
        browser.element("#state").click()
        browser.all('div[class*="option"]').element_by(have.text(state)).click()
        browser.element("#city").click()
        browser.all('div[class*="option"]').element_by(have.text(city)).click()

    def _submit(self):
        browser.element("#submit").click()