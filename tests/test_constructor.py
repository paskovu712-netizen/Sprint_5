import pytest

from pages.login_page import LoginPage
from locators.burger_locators import BurgerLocators
from data_pak import *

class TestBurgerConstructor:

    @pytest.mark.parametrize('buttons,respond',
     [
         [BurgerLocators.SECTION_TEXT_BREAD, 'Булки'],
         [BurgerLocators.SECTION_TEXT_SAUCE, 'Соусы'],
         [BurgerLocators.SECTION_TEXT_TOPPING, 'Начинки']
         ])
    def test_success_move_to_section(self, driver, buttons, respond):
        page = LoginPage(driver)
        page.open_login_page()
        page.login(right_login, right_pass)
        page.click_button(buttons)

        message = page.get_status_section(buttons)
        visible = page.get_visibility_section(buttons)
        
        assert respond in message and visible
   
