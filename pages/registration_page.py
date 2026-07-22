import random
import string

import allure

from locators.registration_page_locators import RegistrationPageLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    @allure.step("Сгенерировать случайную строку")
    def generate_random_string(self, length=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @allure.step("Заполнить имя")
    def set_first_name(self, timeout=10):
        field = self.wait_until_clickable(RegistrationPageLocators.FIRST_NAME_INPUT, timeout)
        field.send_keys(self.generate_random_string())

    @allure.step("Заполнить фамилию")
    def set_last_name(self):
        field = self.driver.find_element(*RegistrationPageLocators.LAST_NAME_INPUT)
        field.send_keys(self.generate_random_string())

    @allure.step("Заполнить логин")
    def set_username(self):
        username = self.generate_random_string()
        field = self.driver.find_element(*RegistrationPageLocators.USERNAME_INPUT)
        field.send_keys(username)
        return username

    @allure.step("Заполнить email")
    def set_email(self):
        email = f'{self.generate_random_string()}@lol.ru'
        field = self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        field.send_keys(email)
        return email

    @allure.step("Заполнить пароль")
    def set_password(self):
        password = f'{self.generate_random_string()}3!'
        field = self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        field.send_keys(password)
        return password

    @allure.step("Нажать на кнопку 'Создать аккаунт'")
    def click_create_account_button(self):
        self.driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()
