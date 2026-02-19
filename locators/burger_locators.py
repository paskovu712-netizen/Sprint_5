from selenium.webdriver.common.by import By

class BurgerLocators:
#  Локаторы Login
# Найди поле "Email"    
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='name'].text.input__textfield.text_type_main-default")
# Найди поле "Пароль"    
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль'].text.input__textfield.text_type_main-default")
# Найди кнопку "Войти"    
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
# Найди кнопку "Войти в аккаунт"
    LOGIN_BUTTON_MAIN = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")
# Найди кнопку "Личный Кабинет"
    PERSONAL_ACCAUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
# Найди кнопку "Оформить заказ"
    MAKE_ORDER_BUTTON = (By.XPATH, ".//div/main/section[2]/div/button")
# Найди кнопку "Зарегистрироваться"
    REGISTRATION_BUTTON = (By.XPATH, ".//div/main/div/div/p[1]/a")
# Найди кнопку "Зарегистрироваться"-"Войти"
    REGISTRATION_LOGIN_BUTTON = (By.XPATH, ".//div/main/div/div/p/a")
# Найди кнопку "Зарегистрироваться"
    RECOVERY_BUTTON = (By.XPATH, ".//div/main/div/div/p[2]/a")
# Найди кнопку "Зарегистрироваться"-"Войти"
    RECOVERY_LOGIN_BUTTON = (By.XPATH, ".//div/main/div/div/p/a")

#  Локаторы Logout
# Найди кнопку "Выход"
    LOGOUT_BUTTON = (By.XPATH, ".//div/main/div/nav/ul/li[3]/button")
# Найди заголовок "Вход"
    LOGIN_PAGE_TEXT = (By.XPATH, ".//div/main/div/h2")

#  Локаторы переходов    
# Найди выбор меню "Профиль"
    PROFILE_MENU_TEXT = (By.XPATH, ".//div/main/div/nav/ul/li[1]/a")
# Найди кнопку "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
# Найди кнопку "Stellar-Burger"
    STELLAR_LOGO_BUTTON = (By.XPATH, ".//div/header/nav/div/a")

# Локаторы регистрации
# Найди кнопку "Зарегистрироваться"
    REGISTRATION_BUTTON = (By.XPATH, ".//div/main/div/div/p[1]/a")
# Найди поле "Имя"
    NAME_INPUT = (By.XPATH, ".//div/main/div/form/fieldset[1]/div/div/input")
# ошибка "Некорректтный пароль"
    ERROR_INVALID_PASSWORD = (By.CSS_SELECTOR, ".input__error.text_type_main-default")

# Локаторы конструктора
# кнопка и текст раздела "Булки"
    SECTION_TEXT_BREAD = (By.XPATH, ".//div/main/section[1]/div[2]/h2[1]")

    SECTION_BUTTON_SAUCE = (By.XPATH, ".//div/main/section[1]/div[1]/div[2]")
# кнопка и текст раздела "Соусы"
    SECTION_TEXT_SAUCE = (By.XPATH, ".//div/main/section[1]/div[2]/h2[2]")
# кнопка и текст раздела "Начинки"
    SECTION_TEXT_TOPPING = (By.XPATH, ".//div/main/section[1]/div[2]/h2[3]")
    