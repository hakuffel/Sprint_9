import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from data import BASE_URL
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


def build_chrome_options():
    options = Options()
    options.add_argument('--disable-save-password-bubble')
    options.add_experimental_option(
        'prefs',
        {
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False,
        }
    )
    return options


def build_local_driver():
    from webdriver_manager.chrome import ChromeDriverManager

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=build_chrome_options())


def build_remote_driver(remote_url):
    return RemoteWebDriver(command_executor=remote_url, options=build_chrome_options())


@pytest.fixture
def driver():
    remote_url = os.environ.get('REMOTE_URL')
    driver = build_remote_driver(remote_url) if remote_url else build_local_driver()

    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def logout_after_test(driver):
    yield
    header_page = HeaderPage(driver)
    if header_page.is_logout_visible():
        header_page.click_logout()


@pytest.fixture
def registered_user(driver):
    header_page = HeaderPage(driver)
    header_page.click_create_account_link()

    registration_page = RegistrationPage(driver)
    registration_page.set_first_name()
    registration_page.set_last_name()
    username = registration_page.set_username()
    registration_page.set_email()
    password = registration_page.set_password()
    registration_page.click_create_account_button()

    login_page = LoginPage(driver)
    login_page.wait_until_redirected_to_auth()

    return username, password


@pytest.fixture
def authorized_driver(driver, registered_user):
    email, password = registered_user

    header_page = HeaderPage(driver)
    header_page.click_enter_link()

    login_page = LoginPage(driver)
    login_page.set_email(email)
    login_page.set_password(password)
    login_page.click_login_button()
    login_page.wait_until_redirected_to_recipes()

    return driver
