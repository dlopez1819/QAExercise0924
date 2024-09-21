import pytest
import time
from src.pages.finance_page import FinancePage
from src.helpers.basepage import BasePage
from src.locators.web_screen_locator import GoogleFinanceScreen

class FinanceData:
    # Given Test Data
    testData = ["NFLX", "MSFT", "TSLA"]

class TestGoogleFinance(BasePage):

    def setUp(self):
        self.driver = self.getDriver()

    @pytest.mark.web
    def test_verify_google_finance_stocks(self):
        #1. Opens a webpage www.google.com/finance on a Chrome browser
        self.setUp()
        #2. Verifies the page is loaded by asserting the page title
        FinancePage.verifyPageLoaded(self)
        time.sleep(2)
        stockList = FinancePage.getElementTextList(self, GoogleFinanceScreen.icnStockList)
        #5. Print all stock symbols that are in (3) but not in given test data
        print("stock list", stockList)
        #4. Compare the stock symbols retrieved from (3) with given test data
        FinancePage.compareStocksSymbols(self, stockList, FinanceData.testData)


