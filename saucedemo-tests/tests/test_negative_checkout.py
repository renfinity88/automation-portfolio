from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def _login_and_go_to_checkout(page: Page, base_url: str):
    lp = LoginPage(page)
    lp.goto(base_url)
    lp.login("standard_user", "secret_sauce")
    page.locator("button[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator(".shopping_cart_link").click()
    page.locator("[data-test='checkout']").click()

def test_checkout_missing_first_name_shows_error(page: Page, base_url: str):
    _login_and_go_to_checkout(page, base_url)
    page.locator("[data-test='lastName']").fill("Tester")
    page.locator("[data-test='postalCode']").fill("60123")
    page.locator("[data-test='continue']").click()
    err = page.locator("[data-test='error']")
    expect(err).to_be_visible()
    expect(err).to_have_text("Error: First Name is required")

def test_checkout_missing_last_name_shows_error(page: Page, base_url: str):
    _login_and_go_to_checkout(page, base_url)
    page.locator("[data-test='firstName']").fill("Reni")
    page.locator("[data-test='postalCode']").fill("60123")
    page.locator("[data-test='continue']").click()
    err = page.locator("[data-test='error']")
    expect(err).to_be_visible()
    expect(err).to_have_text("Error: Last Name is required")

def test_checkout_missing_postal_code_shows_error(page: Page, base_url: str):
    _login_and_go_to_checkout(page, base_url)
    page.locator("[data-test='firstName']").fill("Reni")
    page.locator("[data-test='lastName']").fill("Tester")
    page.locator("[data-test='continue']").click()
    err = page.locator("[data-test='error']")
    expect(err).to_be_visible()
    expect(err).to_have_text("Error: Postal Code is required")

def test_login_locked_out_user_negative(page: Page, base_url: str):
    lp = LoginPage(page)
    lp.goto(base_url)
    lp.login("locked_out_user", "secret_sauce")
    expect(lp.error).to_be_visible()
    expect(lp.error).to_have_text("Epic sadface: Sorry, this user has been locked out.")
