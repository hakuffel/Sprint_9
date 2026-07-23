import allure

from data import RECIPES_URL
from pages.header_page import HeaderPage
from pages.login_page import LoginPage


class TestLogin:

    @allure.title("Проверка авторизации")
    def test_login(self, driver, registered_user, logout_after_test):
        email, password = registered_user

        header_page = HeaderPage(driver)
        header_page.click_enter_link()

        login_page = LoginPage(driver)
        login_page.set_email(email)
        login_page.set_password(password)
        login_page.click_login_button()
        login_page.wait_until_redirected_to_recipes()

        assert login_page.get_current_url() == RECIPES_URL
        assert header_page.is_logout_visible() is True
