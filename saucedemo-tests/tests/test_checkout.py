from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_checkout_order(page: Page, base_url: str):
    # login
    lp = LoginPage(page)
    lp.goto(base_url)
    lp.login("standard_user", "secret_sauce")

    # Tambah item ke cart
    page.locator("button[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator(".shopping_cart_link").click()

    # Proses checkout
    page.locator("[data-test='checkout']").click()
    page.locator("[data-test='firstName']").fill("Reni")
    page.locator("[data-test='lastName']").fill("Tester")
    page.locator("[data-test='postalCode']").fill("60123")
    page.locator("[data-test='continue']").click()

    # Verify summary page → pakai selector spesifik
    expect(page.locator("[data-test='payment-info-label']")).to_have_text("Payment Information:")

    # Selesaikan pesanan
    page.locator("[data-test='finish']").click()
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
