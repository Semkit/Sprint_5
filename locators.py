from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # кнопка "Личный кабинет"
    STELLAR_BURGER_LOGO = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']")  # лого сайта

    REGISTRATION_NAME_FIELD = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")  # поле ввода имени на странице регистрации
    REGISTRATION_EMAIL_FIELD = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")  # поле ввода Email на странице регистрации
    REGISTRATION_PASSWORD_FIELD = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")  # поле ввода пароля на странице регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']")  # кнопка "Зарегистрироваться" на странице регистрации
    INPUT_ERROR_FIELD = (By.XPATH,"//label[text() = 'Пароль']/ancestor::fieldset[contains(@class, 'Auth_fieldset__1QzWN') and contains(@class, 'mb-6')]")  # поле для отображения ошибки по длине пароля на странице регистрации
    REGISTRATION_FORM_LOGIN = (By.XPATH, "//a[@href = '/login']")  # кнопка "Войти" на странице регистрации

    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']")  # кнопка "Войти" на странице входа
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  # кнопка "Войти в аккаунт" на главной странице сайта
    LOGIN_ACCOUNT_HEADER = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # кнопка "Личный Кабинет" на главной странице сайта
    FORGOT_PASSWORD_LOGIN = (By.XPATH, "//a[@href = '/login']")  # кнопка "Войти" на странице Восстановления пароля

    LOGIN_EMAIL_FIELD = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")  # поле ввода Email на странице входа
    LOGIN_PASSWORD_FIELD = REGISTRATION_PASSWORD_FIELD  # поле ввода пароля на странице входа

    CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']") # кнопка "Конструктор"

    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']") # кнопка "Выход"

    BUNS_NO_SELECT = (By.XPATH,"//div[contains (@class, 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect') and span[text() = 'Булки']]")  # вкладка "Булки" не выбрана
    BUNS_SELECTED = (By.XPATH,"//div[contains (@class, 'tab_tab_type_current__') and span[text() = 'Булки']]")  # вкладка "Булки" выбрана
    SAUCE_NO_SELECT = (By.XPATH,"//div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/child::span[text() = 'Соусы']")  # вкладка "Соусы" не выбрана
    SAUCE_SELECTED = (By.XPATH,"//div[contains (@class, 'tab_tab_type_current__') and span[text() = 'Соусы']]")  # вкладка "Соусы" выбрана
    ADDS_NO_SELECT = (By.XPATH,"//div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/child::span[text() = 'Начинки']")  # вкладка "Добавки" не выбрана
    ADDS_SELECTED = (By.XPATH,"//div[contains (@class, 'tab_tab_type_current__') and span[text() = 'Начинки']]")  # вкладка "Добавки" выбрана
