from pages.base_page import BasePage
from locators.burger_locators import BurgerLocators
from curl import BASE_URL, LOGIN_URL, REGISTER_URL


class LoginPage(BasePage):

    def open_main_page(self):
        self.open(BASE_URL)

    def open_login_page(self):
        self.open(LOGIN_URL)

    def open_register_page(self):
        self.open(REGISTER_URL)

    def click_button(self, locator):
        self.click(locator)
    
    def login(self, username, password):
        self.type(BurgerLocators.USERNAME_INPUT, username)
        self.type(BurgerLocators.PASSWORD_INPUT, password)
        self.click(BurgerLocators.LOGIN_BUTTON)

    def register(self, name, username, password):
        self.type(BurgerLocators.NAME_INPUT, name)
        self.type(BurgerLocators.USERNAME_INPUT, username)
        self.type(BurgerLocators.PASSWORD_INPUT, password)
        self.click(BurgerLocators.REGISTRATION_BUTTON)

    def get_status_login(self):
        return self.get_text(BurgerLocators.MAKE_ORDER_BUTTON)

    def get_status_logout(self):
        return self.get_text(BurgerLocators.LOGIN_PAGE_TEXT)
    
    def get_status_account(self):
        return self.get_text(BurgerLocators.PROFILE_MENU_TEXT)
    
    def get_status_error(self):
        return self.get_text(BurgerLocators.ERROR_INVALID_PASSWORD)
    
    def get_status_section(self, locator):
        return self.get_text(locator)
          
    def logout(self):
        self.click(BurgerLocators.PERSONAL_ACCAUNT_BUTTON)
        self.click(BurgerLocators.LOGOUT_BUTTON)
