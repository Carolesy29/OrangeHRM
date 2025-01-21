import os

from selenium.webdriver.common.by import By


class AuthenticationControls:
    INPUT_USERNAME = (By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(2) > div > div:nth-child(2) > input")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(3) > div > div:nth-child(2) > input")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button")
    MENU_RECRUITMENT = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(5) > a")


class RegisterControls:
    PATH = os.getcwd() + '/resources/files/'
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(1) > div > div > div > div.--name-grouped-field > div:nth-child(1) > div:nth-child(2) > input")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(1) > div > div > div > div.--name-grouped-field > div:nth-child(3) > div:nth-child(2) > input")
    INPUT_MIDDLE_NAME = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(1) > div > div > div > div.--name-grouped-field > div:nth-child(2) > div:nth-child(2) > input")
    SELECT_VACANCY = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(2) > div > div > div > div:nth-child(2) > div")
    SELECT_VACANCY_CHILD = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(2) > div > div > div > div:nth-child(2) > div > div.oxd-select-dropdown.--positon-bottom > div:nth-child(3)")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(2) > input")
    INPUT_PHONE = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(3) > div > div:nth-child(2) > div > div:nth-child(2) > input")
    INPUT_CV = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(4) > div > div > div > div > div:nth-child(2) > input")
    INPUT_KEYWORDS = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(5) > div > div.oxd-grid-item.oxd-grid-item--gutters.orangehrm-save-candidate-page-full-width > div > div:nth-child(2) > input")
    INPUT_NOTES = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(6) > div > div > div > div:nth-child(2) > textarea")
    CHECKBOX_CONSENT = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(7) > div > div > div > div:nth-child(2) > div > label > span > i")
    BUTTON_ADD = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div.orangehrm-header-container > button")
    BUTTON_SAVE = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
    TITLE_NAME = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div.orangehrm-card-container > form > h6")
    SPINNER_LOADING = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-loader")
    BUTTON_SHORTLIST = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div.orangehrm-card-container > form > div.orangehrm-recruitment > div.orangehrm-recruitment-actions > button.oxd-button.oxd-button--medium.oxd-button--success")
    BUTTON_SAVE_SHORTLIST = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
    BUTTON_INTERVIEW = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div.orangehrm-card-container > form > div.orangehrm-recruitment > div.orangehrm-recruitment-actions > button.oxd-button.oxd-button--medium.oxd-button--success")
    INPUT_INTERVIEW_TITLE = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > input")
    INPUT_INTERVIEW_DATE = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(2) > div > div:nth-child(3) > div > div:nth-child(2) > div > div > input")
    INPUT_INTERVIEW_TIME = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(2) > div > div:nth-child(4) > div > div:nth-child(2) > div > div > input")
    INPUT_INTERVIEWER = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(2) > div > div:nth-child(2) > div > div > div:nth-child(2) > div > div > input")
    BUTTON_SAVE_INTERVIEW = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
    SELECT_INTERVIEWER = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(2) > div > div:nth-child(2) > div > div > div:nth-child(2) > div > div.oxd-autocomplete-dropdown.--positon-bottom")
    BUTTON_PASSED_INTERVIEW = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div.orangehrm-card-container > form > div.orangehrm-recruitment > div.orangehrm-recruitment-actions > button.oxd-button.oxd-button--medium.oxd-button--success")
    BUTTON_SAVE_PASSED_INTERVIEW = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
    BUTTON_OFFER_JOB = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div.orangehrm-card-container > form > div.orangehrm-recruitment > div.orangehrm-recruitment-actions > button:nth-child(3)")
    BUTTON_SAVE_OFFER_JOB = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
    BUTTON_HIRED = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div.orangehrm-card-container > form > div.orangehrm-recruitment > div.orangehrm-recruitment-actions > button.oxd-button.oxd-button--medium.oxd-button--success")
    BUTTON_SAVE_HIRED = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
    LABEL_HIRED = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[1]/p")
