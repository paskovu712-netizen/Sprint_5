from selenium.webdriver.common.by import By

class BurgerLocators:

# Локаторы регистрации

# Найди кнопку "Войти в аккаунт"
    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
# Найди кнопку "Зарегистрироваться"
    REG_REGISTRATION_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
# Найди поле "Имя"
    REG_NAME_INPUT = (By.CSS_SELECTOR, "input[name='name'].text.input__textfield.text_type_main-default")
# Найди поле "Email"    
    REG_USERNAME_INPUT = (By.CSS_SELECTOR, "form.Auth_form__3qKeq fieldset:nth-child(2) div div input")
# Найди поле "Пароль"    
    REG_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль'].text.input__textfield.text_type_main-default")
# Найди кнопку "Войти"    
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
# ошибка "Некорректный пароль"
    ERROR_INVALID_PASSWORD = (By.CSS_SELECTOR, ".input__error.text_type_main-default")

#  Локаторы Login
# Найди поле "Email"
    LOG_USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='name'].text.input__textfield.text_type_main-default")
# Найди поле "Пароль"    
    LOG_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль'].text.input__textfield.text_type_main-default")
# Найди кнопку "Зарегистрироваться"
    LOG_REGISTRATION_BUTTON = (By.XPATH, ".//a[text()='Зарегистрироваться']")
# Найди кнопку "Личный Кабинет"
    PERSONAL_ACCAUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
# Найди кнопку "Оформить заказ"
    MAKE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
# Найди кнопку "Зарегистрироваться"-"Войти"
    REGISTRATION_LOGIN_BUTTON = (By.XPATH, ".//a[text()='Войти']")
# Найди кнопку "Восстановить пароль"
    RECOVERY_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")
# Найди кнопку "Восстановление пароля"-"Войти"
    RECOVERY_LOGIN_BUTTON = (By.XPATH, ".//a[text()='Войти']")

#  Локаторы Logout

# Найди кнопку "Выход"
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
# Найди заголовок "Вход"
    LOGIN_PAGE_TEXT = (By.XPATH, ".//h2[text()='Вход']")

#  Локаторы переходов
#     
# Найди выбор меню "Профиль"
    PROFILE_MENU_TEXT = (By.XPATH, ".//a[text()='Профиль']")
# Найди кнопку "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
# Найди кнопку "Stellar-Burger"
    STELLAR_LOGO_BUTTON = (By.XPATH, ".//div/header/nav/div/a")

# Локаторы конструктора

# кнопка и текст раздела "Булки"
    SECTION_TEXT_BREAD = (By.XPATH, ".//div[2]/h2[1]") 
# кнопка и текст раздела "Соусы"
    SECTION_TEXT_SAUCE = (By.XPATH, ".//div[2]/h2[2]")
# кнопка и текст раздела "Начинки"
    SECTION_TEXT_TOPPING = (By.XPATH, ".//div[2]/h2[3]")
    