import URLS
from locators import StellarBurgersLocators


class TestLogin:

    def test_login_from_button(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_ACCOUNT_BUTTON).click()
        assert "/login" in driver.current_url

    def test_login_from_account(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_ACCOUNT_HEADER).click()
        assert "/login" in driver.current_url

    def test_login_from_signup_form(self, driver):
        driver.get(URLS.registration_url)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_FORM_LOGIN).click()
        assert "/login" in driver.current_url

    def test_login_from_password_reset_form(self, driver):
        driver.get(URLS.main_url + 'forgot-password')
        driver.find_element(*StellarBurgersLocators.FORGOT_PASSWORD_LOGIN).click()
        assert "/login" in driver.current_url
