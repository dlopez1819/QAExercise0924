import pytest
from selenium import webdriver
import settings


#ToDO
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=settings.browser)
    parser.addoption("--url", action="store", default=settings.url)
    parser.addoption("--env", action="store", default=settings.env)

