import allure

from pages.header_page import HeaderPage
from pages.recipe_page import RecipePage


class TestRecipe:

    @allure.title("Проверка создания рецепта")
    def test_create_recipe(self, authorized_driver, logout_after_test):
        header_page = HeaderPage(authorized_driver)
        header_page.click_create_recipe_link()

        recipe_page = RecipePage(authorized_driver)
        recipe_name = recipe_page.set_recipe_name()
        recipe_page.set_cooking_time()
        recipe_page.set_description()
        recipe_page.upload_image()
        recipe_page.add_ingredient()
        recipe_page.click_create_recipe_button()

        assert recipe_page.is_recipe_card_displayed() is True
        assert recipe_page.get_recipe_title() == recipe_name
