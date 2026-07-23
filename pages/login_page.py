import allure

from data import AUTH_URL, RECIPES_URL
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Заполнить email")
    def set_email(self, email, timeout=10):
        field = self.wait_until_clickable(LoginPageLocators.EMAIL_INPUT, timeout)
        field.send_keys(email)

    @allure.step("Заполнить пароль")
    def set_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажать на кнопку 'Войти'")
    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Дождаться перехода на главную страницу")
    def wait_until_redirected_to_recipes(self, timeout=10):
        self.wait_until_url_to_be(RECIPES_URL, timeout)

    @allure.step("Дождаться перехода на страницу авторизации")
    def wait_until_redirected_to_auth(self, timeout=10):
        self.wait_until_url_to_be(AUTH_URL, timeout)

    @allure.step("Проверить видимость формы авторизации")
    def is_login_form_visible(self, timeout=5):
        return self.is_element_visible(LoginPageLocators.LOGIN_BUTTON, timeout)
