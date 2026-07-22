import random
from pathlib import Path
import os

import allure

from data import INGREDIENT_GRAMS, INGREDIENT_NAME, RECIPE_IMAGE
from locators.recipe_page_locators import RecipePageLocators
from pages.base_page import BasePage

APP_DIR = Path(__file__).parent.parent


class RecipePage(BasePage):

    @allure.step("Ввести название рецепта")
    def set_recipe_name(self, timeout=10):
        name = f'Рецептик номер {random.randint(1000, 9999)}'
        field = self.wait_until_clickable(RecipePageLocators.RECIPE_NAME_INPUT, timeout)
        field.send_keys(name)
        return name

    @allure.step("Ввести время приготовления")
    def set_cooking_time(self):
        field = self.driver.find_element(*RecipePageLocators.COOKING_TIME_INPUT)
        field.send_keys(str(random.randint(5, 200)))

    @allure.step("Ввести описание рецепта")
    def set_description(self):
        field = self.driver.find_element(*RecipePageLocators.DESCRIPTION_TEXTAREA)
        field.send_keys('Очень вкусный рецепт для теста')

    @allure.step("Загрузить фото рецепта")
    def upload_image(self):
        if os.environ.get('REMOTE_URL'):
            file_path = f'/attach/{RECIPE_IMAGE}'
        else:
            file_path = str(APP_DIR / 'attach' / RECIPE_IMAGE)

        image_input = self.driver.find_element(*RecipePageLocators.IMAGE_INPUT)
        image_input.send_keys(file_path)

    @allure.step("Добавить ингредиент из списка")
    def add_ingredient(self, timeout=10):
        ingredient_field = self.wait_until_clickable(RecipePageLocators.INGREDIENT_INPUT, timeout)
        ingredient_field.send_keys(INGREDIENT_NAME)

        first_option = self.wait_until_clickable(RecipePageLocators.FIRST_INGREDIENT_OPTION, timeout)
        first_option.click()

        grams_field = self.driver.find_element(*RecipePageLocators.INGREDIENT_GRAMS_INPUT)
        grams_field.send_keys(INGREDIENT_GRAMS)

        self.driver.find_element(*RecipePageLocators.ADD_INGREDIENT_BUTTON).click()

    @allure.step("Нажать на кнопку 'Создать рецепт'")
    def click_create_recipe_button(self):
        self.driver.find_element(*RecipePageLocators.CREATE_RECIPE_BUTTON).click()

    @allure.step("Проверить отображение карточки созданного рецепта")
    def is_recipe_card_displayed(self, timeout=10):
        return self.is_element_visible(RecipePageLocators.RECIPE_CARD, timeout)

    @allure.step("Получить название рецепта с карточки")
    def get_recipe_title(self, timeout=10):
        title = self.wait_until_visible(RecipePageLocators.RECIPE_TITLE, timeout)
        return title.text
