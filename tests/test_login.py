import pytest

from pages.login_page import LoginPage
from locators.burger_locators import BurgerLocators
from data_pak import *

class TestBurgerLogin:

    @pytest.mark.parametrize('buttons', [BurgerLocators.LOGIN_BUTTON_MAIN, BurgerLocators.PERSONAL_ACCAUNT_BUTTON])
    def test_success_login_by_button_login(self, driver, buttons):
        page = LoginPage(driver)
        page.open_main_page()
        page.click_button(buttons)
        page.login(right_login, right_pass)
        
        message = page.get_status_login()
        assert 'Оформить заказ' in message

    def test_success_login_by_button_login_registration(self, driver):
        page = LoginPage(driver)
        page.open_main_page()
        page.click_button(BurgerLocators.LOGIN_BUTTON_MAIN)
        page.click_button(BurgerLocators.REGISTRATION_BUTTON)
        page.click_button(BurgerLocators.REGISTRATION_LOGIN_BUTTON)
        page.login(right_login, right_pass)
        
        message = page.get_status_login()
        assert 'Оформить заказ' in message

    def test_success_login_by_button_login_recover(self, driver):
        page = LoginPage(driver)
        page.open_main_page()
        page.click_button(BurgerLocators.LOGIN_BUTTON_MAIN)
        page.click_button(BurgerLocators.RECOVERY_BUTTON)
        page.click_button(BurgerLocators.RECOVERY_LOGIN_BUTTON)
        page.login(right_login, right_pass)
        
        message = page.get_status_login()
        assert 'Оформить заказ' in message
