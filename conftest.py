import pytest
from selene import browser

@pytest.fixture(scope="session", autouse=True)
def configure_browser():
    # Настройка браузера
    browser.config.window_height = 1000
    browser.config.window_width = 1200
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com'

    yield

    # Закрываем браузер после завершения всех тестов
    browser.quit()