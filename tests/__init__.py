import os

from tests.pages.hired.authentication import Authentication
from tests.pages.hired.register import Register
from tests.pages.orange_hrm import OrangeHrm


class FlowHired:
    authentication = Authentication()
    register = Register()

    def __init__(self):
        self.web = OrangeHrm()

    def open_page(self, browser):
        self.web.set_browser(browser)
        self.web.open_url(os.environ.get("BASE_URL") + '/auth/login')

    def quit_page(self):
        self.web.quit_browser()
