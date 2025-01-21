import json
import time
import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class OrangeHrm:

    def __init__(self):
        self.re_xpath = "^[^/,(,.].*"
        self.timestamp = time.time()

    @property
    def driver(self):
        return driver

    def set_browser(self, browser):
        global driver

        capabilities = open("resources/devices/macosx.json")
        capabilities = json.load(capabilities)

        path = os.getcwd() + '/chromedriver'
        
        driver = webdriver.Chrome(executable_path=path, desired_capabilities=capabilities)
        driver.maximize_window()

    def quit_browser(self):
        try:
            yield driver
            driver.quit()
        except Exception:
            print("info: Another process has already closed the app process.")

    @staticmethod
    def open_url(url):
        driver.get(str(url))

    def wait_displayed_element(self, element_locator, retries=60):
        element = None
        for _ in range(retries):
            try:
                time.sleep(1)
                element = self.find_element(element_locator)
                if element.is_displayed():
                    break
            except Exception:
                pass
        return element

    def input_text(self, element_locator, text):
        self.wait_present_element(element_locator).send_keys(text)

    def find_element(self, element_locator):
        return driver.find_element(*element_locator)

    def wait_present_element(self, element_locator, retries=60):
        return WebDriverWait(driver, retries).until(ec.presence_of_element_located(element_locator))

    def wait_interactable_element(self, element_locator, retries=60):
        element = None
        for _ in range(retries):
            try:
                time.sleep(1)
                element = self.find_element(element_locator)
                if element.is_enabled():
                    break
            except Exception:
                pass
        return element

    def format(self, element_locator, text):
        element_type = element_locator[0]
        element_locator = element_locator[1].format(text)
        return (element_type, element_locator)

    def select_option(self, element_locator):
        element = self.driver.find_element(element_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()

    def wait_for_page_load(self, element_locator, timeout=60):
        WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located(element_locator)
        )

    def wait_for_loading_to_finish(self, element_locator, timeout=60):
        WebDriverWait(driver, timeout).until(
            ec.invisibility_of_element_located(element_locator)
        )

    def get_text(self, element_locator):
        element = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(element_locator)
        )

        if element:
            return element.text
        return ''
