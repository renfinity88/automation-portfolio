from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_checkout_full_summary_and_finish(page: Page, base_url: str):
    # Login
    lp = LoginPage(page)
    lp.goto(base_url)
    lp.login("standard_user", "secret_sauce")

    # Tambah 2 item
    page.locator("button[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator("button[data-test='add-to-cart-sauce-labs-bike-light']").click()

    # Masuk cart
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".cart_item")).to_have_count(2)

    # Checkout
    page.locator("[data-test='checkout']").click()
    page.locator("[data-test='firstName']").fill("Reni")
    page.locator("[data-test='lastName']").fill("Tester")
    page.locator("[data-test='postalCode']").fill("60123")
    page.locator("[data-test='continue']").click()

    # ====== Verifikasi ringkasan ======
    expect(page.locator("[data-test='payment-info-label']")).to_have_text("Payment Information:")
    expect(page.locator("[data-test='shipping-info-label']")).to_have_text("Shipping Information:")
    expect(page.locator("[data-test='total-info-label']")).to_contain_text("Price Total")

    # Subtotal, Tax, Total
    expect(page.locator(".summary_subtotal_label")).to_contain_text("Item total: $")
    expect(page.locator(".summary_tax_label")).to_contain_text("Tax: $")
    expect(page.locator(".summary_total_label")).to_contain_text("Total: $")

    # Selesaikan pesanan
    page.locator("[data-test='finish']").click()
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
