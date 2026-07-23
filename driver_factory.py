from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

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