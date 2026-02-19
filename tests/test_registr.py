import pytest

from pages.login_page import LoginPage
from locators.burger_locators import BurgerLocators
from data_pak import *

def test_success_registration(driver):
    page = LoginPage(driver)
    page.open_register_page()
    page.register(right_name, page.email_new(), right_pass)
    
    message = page.get_status_logout()
    assert 'Вход' in message
    
def test_invalid_registration_wrong_password(driver):
    page = LoginPage(driver)
    page.open_register_page()
    page.register(right_name, page.email_new(), wrong_pass)
    
    message = page.get_status_error()
    assert 'Некорректный пароль' in message
        