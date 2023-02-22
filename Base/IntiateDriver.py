from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from Library import ConfigReader
from selenium.webdriver import Firefox


def startBrowser():

    global driver

    # to keep the browser open we use option class
    options = Options()
    options.add_experimental_option("detach", True)

    if((ConfigReader.readConfigData('Details', 'Browser')) == 'Chrome'):
        # create an object of the class Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif((ConfigReader.readConfigData('Details', 'Browser')) == 'Firefox'):
        path ="Users\\chine\\Desktop\\firefoxdriver.exe"
        driver = Firefox(executable_path=path)
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # calling get method to enter url
    driver.get(ConfigReader.readConfigData('Details', 'Application_URL'))

    # maximize window
    driver.maximize_window()

    #return driver
    return driver


def closeBrowser():
    time.sleep(20)
    driver.close()
