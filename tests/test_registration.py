from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import URLS
import data_generator
from locators import StellarBurgersLocators


class TestBurgerRegistration:

    def test_successful_registration(self, driver):
        driver.get(URLS.registration_url)
        login = data_generator.generate_login()
        password = data_generator.generate_password()
        name_input = driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_FIELD)
        name_input.send_keys('Ivan')

        login_input = driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_FIELD)
        login_input.send_keys(login)

        password_input = driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_FIELD)
        password_input.send_keys(password)

        registration_button = driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON)
        registration_button.click()

        WebDriverWait(driver, 5).until(EC.url_to_be(URLS.login_url))

        assert '/login' in driver.current_url

    def test_minimum_password_length(self, driver):
        driver.get(URLS.registration_url)
        login = data_generator.generate_login()
        password = '12345'
        name_input = driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_FIELD)
        name_input.send_keys('Ivan')

        login_input = driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_FIELD)
        login_input.send_keys(login)

        password_input = driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_FIELD)
        password_input.send_keys(password)

        registration_button = driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON)
        registration_button.click()

        assert 'Некорректный пароль' in driver.find_element(*StellarBurgersLocators.INPUT_ERROR_FIELD).text
