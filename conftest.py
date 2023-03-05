from selenium import webdriver
import pytest


#However, the approach comes with its own limitation. A fixture function defined inside a test file has a scope within the test file only. We cannot use that fixture in another test file.
#To make a fixture available to multiple test files, we have to define the fixture function in a file called conftest.py. conftest.py

@pytest.fixture()
def setup(browser):

    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser=='firefox':
        print("launching firefox Browser")
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Ie()
        print("Launching Internet Explorer")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name']='Commerce_Project'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Pavan'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)









