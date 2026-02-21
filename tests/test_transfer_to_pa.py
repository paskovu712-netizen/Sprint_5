import pytest

from pages.login_page import LoginPage
from locators.burger_locators import BurgerLocators
from data_pak import *

class TestBurgerTransfer_to_pa:

    def test_success_transfer_to_personal_account(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.login(right_login, right_pass)
        page.click_button(BurgerLocators.PERSONAL_ACCAUNT_BUTTON)

        message = page.get_status_account()
        assert 'Профиль' in message
