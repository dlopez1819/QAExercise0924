import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from src.helpers.basepage import BasePage


class PageObject(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def wait_for(self, locator):
        wait = WebDriverWait(self.driver, 2)
        return self.wait.until(EC.visibility_of_element_located(locator))

    def element(self, locator):
        wait = WebDriverWait(self.driver, 2)
        self.wait.until(EC.visibility_of_element_located(locator))
        try:
            return self.driver.find_element(*locator)
        except Exception as e:
            self.logger.error(f"element not found  - {locator}")

    def list_elements(self, locator):
        wait = WebDriverWait(self.driver, 2)
        try:
            wait.until(EC.visibility_of_any_elements_located(locator))
            return self.driver.find_elements(*locator)
        except Exception as e:
            self.logger.error(f"element not found  - {locator}")

    def is_displayed(self, locator, expected=True):
        wait = WebDriverWait(self.driver, 2)
        try:
            self.wait.until(EC.visibility_of_any_elements_located(locator))
            assert self.driver.find_elements(*locator).is_displayed() == expected
            return expected
        except Exception as e:
            print(f'is_displayed failed attempt {locator}')
            self.logger.error(f'is_displayed failed attempt{locator}')

    def click(self, locator):
        wait = WebDriverWait(self.driver, 2)
        wait .until(EC.presence_of_element_located(locator)).click()

    def alert(self):
        return self.wait.until(ec.alert_is_present())


