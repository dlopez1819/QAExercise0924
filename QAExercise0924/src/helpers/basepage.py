import pytest
from selenium import webdriver
import settings

driver = None
class BasePage():

    def getDriver(self):
        global driver
        driver = webdriver.Chrome()
        driver.get(settings.url)
        # yield driver
        #driver.close()
        return driver
