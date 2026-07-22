from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_until_present(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_until_url_to_be(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )

    def wait_until_number_of_elements(self, locator, count, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.find_elements(*locator)) >= count
        )

    def is_element_visible(self, locator, timeout=5):
        elements = WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_elements(*locator)
        )
        return any(element.is_displayed() for element in elements) if elements else False

    def get_current_url(self):
        return self.driver.current_url
