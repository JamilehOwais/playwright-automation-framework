# ==========================================
# FILE: pages/checkout_page.py
# ==========================================
from playwright.sync_api import Page
class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.error_message = page.locator("[data-test='error']")
    def fill_checkout_info(self, first, last, postal):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)
        self.continue_button.click()