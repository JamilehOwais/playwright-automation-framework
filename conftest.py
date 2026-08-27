import os
import pytest
from playwright.sync_api import Page, Browser
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()
@pytest.fixture
def logged_in_page(page: Page):
    login_page = LoginPage(page)
    page.goto(os.getenv("BASE_URL"))
    login_page.login(os.getenv("SAUCE_USERNAME"), os.getenv("SAUCE_PASSWORD"))
    yield page
    print("\n[Teardown]: Closing browser safely.")


@pytest.fixture
def api_logged_in_page(browser: Browser):
    context = browser.new_context()
    context.add_cookies([{
        "name": "session-username",
        "value": os.getenv("SAUCE_USERNAME"),
        "url": os.getenv("BASE_URL")
    }])
    page = context.new_page()
    page.goto(f"{os.getenv('BASE_URL')}/inventory.html")
    yield page
    context.close()