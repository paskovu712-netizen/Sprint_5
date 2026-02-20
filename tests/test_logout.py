import pytest

from pages.login_page import LoginPage
from locators.burger_locators import BurgerLocators
from data_pak import *
   
class TestBurgerLogout:
    def test_success_logout(self, driver):
        page = LoginPage(driver)
        page.open_main_page()
        page.click_button(BurgerLocators.LOGIN_BUTTON_MAIN)
        page.login(right_login, right_pass)
        page.logout()
        
        message = page.get_status_logout()
        assert 'Вход' in message
