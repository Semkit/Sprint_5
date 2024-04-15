from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import URLS
from data_generator import cred_login
from data_generator import cred_pass
from locators import StellarBurgersLocators


class TestTransitions:

    def test_go_to_account_page(self, driver):
        driver.get(URLS.login_url)
        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FIELD).send_keys(cred_login)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(cred_pass)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(URLS.main_url))
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT).click()
        assert '/account' in driver.current_url

    def test_go_to_constructor_from_account_page(self, driver):
        driver.get(URLS.login_url)
        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FIELD).send_keys(cred_login)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(cred_pass)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        driver.find_element(*StellarBurgersLocators.CONSTRUCTOR).click()

        assert driver.current_url == URLS.main_url

    def test_go_to_builder_from_account_page_logo(self, driver):
        driver.get(URLS.login_url)
        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FIELD).send_keys(cred_login)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(cred_pass)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        driver.find_element(*StellarBurgersLocators.STELLAR_BURGER_LOGO).click()

        assert driver.current_url == URLS.main_url

    def test_logout_from_account(self, driver):
        driver.get(URLS.login_url)
        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FIELD).send_keys(cred_login)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_FIELD).send_keys(cred_pass)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(URLS.login_url))
        assert driver.current_url == URLS.login_url


class TestConstructor:

    def test_buns_to_sauce(self, driver):
        driver.get(URLS.main_url)
        buns_is_selected = driver.find_element(*StellarBurgersLocators.BUNS_SELECTED).get_attribute('class')
        driver.find_element(*StellarBurgersLocators.SAUCE_NO_SELECT).click()
        sauce_is_selected = driver.find_element(*StellarBurgersLocators.SAUCE_SELECTED).get_attribute('class')
        assert buns_is_selected == sauce_is_selected

    def test_buns_to_adds(self, driver):
        driver.get(URLS.main_url)
        buns_is_selected = driver.find_element(*StellarBurgersLocators.BUNS_SELECTED).get_attribute('class')
        driver.find_element(*StellarBurgersLocators.ADDS_NO_SELECT).click()
        adds_is_selected = driver.find_element(*StellarBurgersLocators.ADDS_SELECTED).get_attribute('class')
        assert buns_is_selected == adds_is_selected

    def test_adds_to_sauce(self, driver):
        driver.get(URLS.main_url)
        driver.find_element(*StellarBurgersLocators.ADDS_NO_SELECT).click()
        adds_is_selected = driver.find_element(*StellarBurgersLocators.ADDS_SELECTED).get_attribute('class')
        driver.find_element(*StellarBurgersLocators.SAUCE_NO_SELECT).click()
        sauce_is_selected = driver.find_element(*StellarBurgersLocators.SAUCE_SELECTED).get_attribute('class')
        assert adds_is_selected == sauce_is_selected

    def test_adds_to_buns(self, driver):
        driver.get(URLS.main_url)
        driver.find_element(*StellarBurgersLocators.ADDS_NO_SELECT).click()
        adds_is_selected = driver.find_element(*StellarBurgersLocators.ADDS_SELECTED).get_attribute('class')
        driver.find_element(*StellarBurgersLocators.BUNS_NO_SELECT).click()
        buns_is_selected = driver.find_element(*StellarBurgersLocators.BUNS_SELECTED).get_attribute('class')
        assert adds_is_selected == buns_is_selected

    def test_sauce_to_buns(self, driver):
        driver.get(URLS.main_url)
        buns_is_selected = driver.find_element(*StellarBurgersLocators.BUNS_SELECTED).get_attribute('class')
        driver.find_element(*StellarBurgersLocators.SAUCE_NO_SELECT).click()
        sauce_is_selected = driver.find_element(*StellarBurgersLocators.SAUCE_SELECTED).get_attribute('class')
        buns_now_not_selected = driver.find_element(*StellarBurgersLocators.BUNS_NO_SELECT).get_attribute('class')
        driver.find_element(*StellarBurgersLocators.BUNS_NO_SELECT).click()
        buns_is_selected_again = driver.find_element(*StellarBurgersLocators.BUNS_SELECTED).get_attribute('class')

        assert buns_is_selected == sauce_is_selected == buns_is_selected_again != buns_now_not_selected

    def test_sauce_to_adds(self, driver):
        driver.get(URLS.main_url)
        buns_is_selected = driver.find_element(*StellarBurgersLocators.BUNS_SELECTED).get_attribute('class')
        driver.find_element(*StellarBurgersLocators.SAUCE_NO_SELECT).click()
        sauce_is_selected = driver.find_element(*StellarBurgersLocators.SAUCE_SELECTED).get_attribute('class')
        buns_now_not_selected = driver.find_element(*StellarBurgersLocators.BUNS_NO_SELECT).get_attribute('class')
        driver.find_element(*StellarBurgersLocators.BUNS_NO_SELECT).click()
        buns_is_selected_again = driver.find_element(*StellarBurgersLocators.BUNS_SELECTED).get_attribute('class')

        assert buns_is_selected == sauce_is_selected == buns_is_selected_again != buns_now_not_selected
