# page_objects/registration_page.py
from selene import browser, have, by
import os


class RegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)
        return self

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)
        return self

    def fill_user_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def select_gender(self, gender):
        # gender: 1 = Male, 2 = Female, 3 = Other
        browser.element(f'label[for="gender-radio-{gender}"]').click()
        return self

    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)
        return self

    def set_birth_date(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').element(by.text(str(year))).click()
        browser.element('.react-datepicker__month-select').element(by.text(month)).click()
        browser.all('.react-datepicker__day:not(.react-datepicker__day--outside-month)').element_by(
            have.exact_text(str(day))
        ).click()
        return self

    def fill_subjects(self, subjects):
        browser.element('#subjectsInput').type(subjects).press_enter()
        return self

    def select_hobby(self, hobby_id):
        # hobby_id: 1 = Sports, 2 = Reading, 3 = Music
        browser.element(f'label[for="hobbies-checkbox-{hobby_id}"]').click()
        return self

    def upload_picture(self, image_name):
        image_path = self.get_image_path(image_name)
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Изображение не найдено по пути: {image_path}")
        browser.element('#uploadPicture').send_keys(image_path)
        return self

    def get_image_path(self, image_name):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, '..', 'tests', image_name)
        return os.path.abspath(image_path)

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def select_state(self, state):
        browser.element('#state').click()
        browser.all('div[class*="option"]').element_by(have.text(state)).click()
        return self

    def select_city(self, city):
        browser.element('#city').click()
        browser.all('div[class*="option"]').element_by(have.text(city)).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_registered(
        self,
        first_name,
        last_name,
        email,
        phone_number,
        birth_date,
        subject,
        hobby,
        address,
        state_and_city
    ):
        full_name = f"{first_name} {last_name}"
        modal = browser.element('.modal-body')
        modal.should(have.text(full_name))
        modal.should(have.text(email))
        modal.should(have.text(phone_number))
        modal.should(have.text(birth_date))
        modal.should(have.text(subject))
        modal.should(have.text(hobby))
        modal.should(have.text(address))
        modal.should(have.text(state_and_city))
        return self