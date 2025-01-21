from tests.pages.hired.__locators__ import RegisterControls
from tests.pages.orange_hrm import OrangeHrm


class Register(OrangeHrm):

    def __init__(self):
        OrangeHrm.__init__(self)
        self.register_control = RegisterControls

    def first_name(self, firstname="Esymar"):
        for _ in range(60):
            if self.wait_displayed_element(self.register_control.INPUT_FIRSTNAME, 1):
                self.input_text(self.register_control.INPUT_FIRSTNAME, firstname)
                break

    def last_name(self, lastname="Vega"):
        for _ in range(60):
            if self.wait_displayed_element(self.register_control.INPUT_LASTNAME, 1):
                self.input_text(self.register_control.INPUT_LASTNAME, lastname)
                break

    def middle_name(self, middle_name="Carolina"):
        for _ in range(60):
            if self.wait_displayed_element(self.register_control.INPUT_MIDDLE_NAME, 1):
                self.input_text(self.register_control.INPUT_MIDDLE_NAME, middle_name)
                break

    def email(self, email="myemail@email.com"):
        for _ in range(60):
            if self.wait_displayed_element(self.register_control.INPUT_EMAIL, 1):
                self.input_text(self.register_control.INPUT_EMAIL, email)
                break

    def phone(self, phone="66666666"):
        for _ in range(60):
            if self.wait_displayed_element(self.register_control.INPUT_PHONE, 1):
                self.input_text(self.register_control.INPUT_PHONE, phone)
                break

    def keywords(self, keywords="payroll, administrator"):
        for _ in range(60):
            if self.wait_displayed_element(self.register_control.INPUT_KEYWORDS, 1):
                self.input_text(self.register_control.INPUT_KEYWORDS, keywords)
                break

    def notes(self, notes="confirmed"):
        for _ in range(60):
            if self.wait_displayed_element(self.register_control.INPUT_NOTES, 1):
                self.input_text(self.register_control.INPUT_NOTES, notes)
                break

    def interview_title(self, title="Interview"):
        for _ in range(60):
            if self.wait_displayed_element(self.register_control.INPUT_INTERVIEW_TITLE, 1):
                self.input_text(self.register_control.INPUT_INTERVIEW_TITLE, title)
                break

    def interview_date(self, date="2021-12-31"):
        for _ in range(60):
            if self.wait_displayed_element(self.register_control.INPUT_INTERVIEW_DATE, 1):
                self.input_text(self.register_control.INPUT_INTERVIEW_DATE, date)
                break

    def interview_time(self, appointment="12:00"):
        for _ in range(60):
            if self.wait_displayed_element(self.register_control.INPUT_INTERVIEW_TIME, 1):
                self.input_text(self.register_control.INPUT_INTERVIEW_TIME, appointment)
                break

    def interviewer(self, interviewer="a"):
        for _ in range(60):
            if self.wait_displayed_element(self.register_control.INPUT_INTERVIEWER, 1):
                self.input_text(self.register_control.INPUT_INTERVIEWER, interviewer)
                element = self.wait_interactable_element(self.register_control.SELECT_INTERVIEWER)
                if element:
                    element.click()
                break

    def select_vacancy(self):
        select = self.wait_interactable_element(self.register_control.SELECT_VACANCY)
        if select:
            select.click()
            element = self.wait_interactable_element(self.register_control.SELECT_VACANCY_CHILD)
            if element:
                element.click()

    def upload(self, path):
        self.input_text(self.register_control.INPUT_CV, self.register_control.PATH + path)

    def click_consent(self):
        element = self.wait_interactable_element(self.register_control.CHECKBOX_CONSENT)
        if element:
            element.click()

    def click_add(self):
        element = self.wait_interactable_element(self.register_control.BUTTON_ADD)
        if element:
            element.click()

    def click_save(self):
        element = self.wait_interactable_element(self.register_control.BUTTON_SAVE)
        if element:
            element.click()

    def click_shortlist(self):
        element = self.wait_interactable_element(self.register_control.BUTTON_SHORTLIST)
        if element:
            element.click()

    def click_save_shortlist(self):
        element = self.wait_interactable_element(self.register_control.BUTTON_SAVE_SHORTLIST)
        if element:
            element.click()

    def click_schedule_interview(self):
        element = self.wait_interactable_element(self.register_control.BUTTON_INTERVIEW)
        if element:
            element.click()

    def click_save_schedule_interview(self):
        element = self.wait_interactable_element(self.register_control.BUTTON_SAVE_INTERVIEW)
        if element:
            element.click()

    def click_passed_interview(self):
        element = self.wait_interactable_element(self.register_control.BUTTON_PASSED_INTERVIEW)
        if element:
            element.click()

    def click_save_passed_interview(self):
        element = self.wait_interactable_element(self.register_control.BUTTON_SAVE_PASSED_INTERVIEW)
        if element:
            element.click()

    def click_offer_job(self):
        element = self.wait_interactable_element(self.register_control.BUTTON_OFFER_JOB)
        if element:
            element.click()

    def click_save_offer_job(self):
        element = self.wait_interactable_element(self.register_control.BUTTON_SAVE_OFFER_JOB)
        if element:
            element.click()

    def click_hired_button(self):
        element = self.wait_interactable_element(self.register_control.BUTTON_HIRED)
        if element:
            element.click()

    def click_save_hired_button(self):
        element = self.wait_interactable_element(self.register_control.BUTTON_SAVE_HIRED).click()
        if element:
            element.click()

    def verify_hired(self, retries=60):
        element = self.wait_displayed_element(self.register_control.LABEL_HIRED, retries)
        if element:
            element = element.text
        return element
