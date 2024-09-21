from src.helpers.pageobject import PageObject
from selenium.webdriver.common.by import By
from src.helpers.basepage import BasePage

class GoogleFinanceScreen(BasePage):
    icnStockList = (By.CLASS_NAME, "COaKTb")
    btnLocalMarket = (By.CLASS_NAME, "GqNdIe ")
