import os
from playwright.sync_api import Page, expect

from pages.checkout_page import CheckoutPage


def test_fast_checkout(api_logged_in_page:Page):
    # 1. Add backpack to cart directly from inventory
    api_logged_in_page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    # 2. Go to cart and click checkout
    api_logged_in_page.locator("[data-test='shopping-cart-link']").click()
    api_logged_in_page.locator("[data-test='checkout']").click()

    # 3. Retrieve TEST_BUYER from .env
    buyer_name = os.getenv("TEST_BUYER")

    # 4. Initialize CheckoutPage using pages/checkout_page.py
    checkout_page = CheckoutPage(api_logged_in_page)

    # 5. Fill the First Name field (or complete the form using fill_checkout_info)
    checkout_page.first_name.fill(buyer_name)
    expect (checkout_page.first_name).to_have_value("Jamila")