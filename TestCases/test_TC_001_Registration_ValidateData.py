from Base import IntiateDriver
from Pages import RegistrationPage
import pytest


def dataGenerator():
    li =[['uname1', 'pass1'],['uname2', 'pass2'],['uname3', 'pass3']]
    return li


@pytest.mark.parametrize('data', dataGenerator())
def test_ValidateRegistration(data):
    driver = IntiateDriver.startBrowser()
    registration = RegistrationPage.RegistrationClass(driver)
    registration.enter_username(data[0])
    registration.enter_email("chin@gmail.com")
    registration.enter_password(data[1])


    IntiateDriver.closeBrowser()