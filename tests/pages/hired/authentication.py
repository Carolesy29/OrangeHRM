from tests.pages.hired.__locators__ import AuthenticationControls
from tests.pages.orange_hrm import OrangeHrm


class Authentication(OrangeHrm):

    def __init__(self):
        OrangeHrm.__init__(self)
        self.authentication_control = AuthenticationControls

    def user_name(self, username="Admin"):
        for _ in range(60):
            if self.wait_displayed_element(self.authentication_control.INPUT_USERNAME, 1):
                self.input_text(self.authentication_control.INPUT_USERNAME, username)
                break

    def password(self, password="admin123"):
        self.input_text(self.authentication_control.INPUT_PASSWORD, password)

    def login(self):
        self.wait_interactable_element(self.authentication_control.BUTTON_LOGIN).click()

    def make_click_recruitment(self):
        self.wait_interactable_element(self.authentication_control.MENU_RECRUITMENT).click()
