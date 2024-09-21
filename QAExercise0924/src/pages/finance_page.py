import time
from src.helpers.basepage import BasePage
from src.helpers.pageobject import PageObject
from src.locators.web_screen_locator import GoogleFinanceScreen

class FinancePage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def getPageTitle(self):
        return self.driver.title

    def verifyPageLoaded(self):
        title = FinancePage.getPageTitle(self)
        assert "Google Finance" in title, "Getting Page Title Success"

    def getElementTextList(self, locator):
        #PageObject.click(self, locator)
        ele_list = []
        eleList = PageObject.list_elements(self, locator=locator)
        for ele in eleList:
            ele_text = ele.text
            ele_list.append(ele_text)
        return ele_list

    def compareStocksSymbols(self, stockList, testData):
        print("testData", testData)
        print(len(testData))
        print(len(stockList))
        new_testdata = []
        not_testData = []
        for i in range(0, len(stockList)):
            for j in range(0, len(testData)):
                if testData[j] in stockList[i]:
                    new_testdata.append(stockList[i])
            if not testData[j] in stockList[i]:
                not_testData.append(stockList[i])
        #6. Print all stock symbols that are in given test data but not in (3)
        print("compared testData", new_testdata)
        #5. Print all stock symbols that are in (3) but not in given test data
        print("not testData", not_testData)






