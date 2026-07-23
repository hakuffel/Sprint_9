from selenium.webdriver.common.by import By


class HeaderPageLocators:

    CREATE_ACCOUNT_LINK = (By.XPATH, "//header//a[contains(text(), 'Создать аккаунт')]")

    ENTER_LINK = (By.XPATH, "//header//a[contains(text(), 'Войти')]")

    CREATE_RECIPE_LINK = (By.XPATH, "//header//a[contains(text(), 'Создать рецепт')]")

    LOGOUT_BUTTON = (By.XPATH, "//header//a[contains(text(), 'Выход')]")
