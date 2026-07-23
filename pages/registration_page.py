import allure

from locators.registration_page_locators import RegistrationPageLocators
from pages.base_page import BasePage
from helpers import generate_random_string


class RegistrationPage(BasePage):

    @allure.step("Заполнить имя")
    def set_first_name(self, timeout=10):
        field = self.wait_until_clickable(RegistrationPageLocators.FIRST_NAME_INPUT, timeout)
        field.send_keys(generate_random_string())

    @allure.step("Заполнить фамилию")
    def set_last_name(self):
        self.send_keys(RegistrationPageLocators.LAST_NAME_INPUT, generate_random_string())

    @allure.step("Заполнить логин")
    def set_username(self):
        username = generate_random_string()
        self.send_keys(RegistrationPageLocators.USERNAME_INPUT, username)
        return username

    @allure.step("Заполнить email")
    def set_email(self):
        email = f'{generate_random_string()}@lol.ru'
        self.send_keys(RegistrationPageLocators.EMAIL_INPUT, email)
        return email

    @allure.step("Заполнить пароль")
    def set_password(self):
        password = f'{generate_random_string()}3!'
        self.send_keys(RegistrationPageLocators.PASSWORD_INPUT, password)
        return password

    @allure.step("Нажать на кнопку 'Создать аккаунт'")
    def click_create_account_button(self):
        self.click(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)
