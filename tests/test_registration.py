import allure

from data import AUTH_URL
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


class TestRegistration:

    @allure.title("Проверка создания аккаунта")
    def test_create_account(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_create_account_link()

        registration_page = RegistrationPage(driver)
        registration_page.set_first_name()
        registration_page.set_last_name()
        registration_page.set_username()
        registration_page.set_email()
        registration_page.set_password()
        registration_page.click_create_account_button()

        login_page = LoginPage(driver)
        login_page.wait_until_redirected_to_auth()

        assert login_page.get_current_url() == AUTH_URL
        assert login_page.is_login_form_visible() is True
