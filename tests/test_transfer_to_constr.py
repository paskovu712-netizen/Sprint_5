import pytest

from pages.login_page import LoginPage
from locators.burger_locators import BurgerLocators
from data_pak import *

class TestBurgerTransfer_to_constr:

    @pytest.mark.parametrize('buttons', [BurgerLocators.CONSTRUCTOR_BUTTON, BurgerLocators.STELLAR_LOGO_BUTTON])
    def test_success_transfer_from_personal_account_to_constructor(self,driver, buttons):
        page = LoginPage(driver)
        page.open_login_page()
        page.login(right_login, right_pass)
        page.click_button(buttons)
        
        message = page.get_status_login()
        assert 'Оформить заказ' in message
        