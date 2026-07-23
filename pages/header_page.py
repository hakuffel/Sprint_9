import allure

from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step("Нажать 'Создать аккаунт' в шапке")
    def click_create_account_link(self, timeout=10):
        link = self.wait_until_clickable(HeaderPageLocators.CREATE_ACCOUNT_LINK, timeout)
        link.click()

    @allure.step("Нажать 'Войти' в шапке")
    def click_enter_link(self, timeout=10):
        link = self.wait_until_clickable(HeaderPageLocators.ENTER_LINK, timeout)
        link.click()

    @allure.step("Перейти на таб 'Создать рецепт'")
    def click_create_recipe_link(self, timeout=10):
        link = self.wait_until_clickable(HeaderPageLocators.CREATE_RECIPE_LINK, timeout)
        link.click()

    @allure.step("Нажать на кнопку 'Выход'")
    def click_logout(self):
        self.click(HeaderPageLocators.LOGOUT_BUTTON)

    @allure.step("Проверить видимость кнопки 'Выход'")
    def is_logout_visible(self, timeout=5):
        return self.is_element_visible(HeaderPageLocators.LOGOUT_BUTTON, timeout)
