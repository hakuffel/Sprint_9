from selenium.webdriver.common.by import By


class RecipePageLocators:

    RECIPE_NAME_INPUT = (By.XPATH, "//*[contains(text(), 'Название рецепта')]/ancestor::label//input")

    COOKING_TIME_INPUT = (By.XPATH, "//*[contains(text(), 'Время приготовления')]/ancestor::label//input")

    DESCRIPTION_TEXTAREA = (By.XPATH, "//*[contains(text(), 'Описание рецепта')]/ancestor::label//textarea")

    IMAGE_INPUT = (By.CSS_SELECTOR, "input[type='file']")

    INGREDIENT_INPUT = (By.XPATH, "//*[contains(text(), 'Ингредиенты')]/ancestor::label//input")

    FIRST_INGREDIENT_OPTION = (By.CSS_SELECTOR, "div.styles_container__3ukwm > div:first-child")

    INGREDIENT_GRAMS_INPUT = (By.CSS_SELECTOR, "input.styles_ingredientsAmountValue__2matT")

    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[contains(text(), 'Добавить ингредиент')]")

    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать рецепт')]")

    RECIPE_CARD = (By.CSS_SELECTOR, "div.styles_single-card__info__2_cny")

    RECIPE_TITLE = (By.TAG_NAME, "h1")
