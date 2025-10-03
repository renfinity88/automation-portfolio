from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(page: Page, base_url: str):
    # login dulu
    lp = LoginPage(page)
    lp.goto(base_url)
    lp.login("standard_user", "secret_sauce")

    inv = InventoryPage(page)

    # Tambah 2 produk pertama
    page.locator("button[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator("button[data-test='add-to-cart-sauce-labs-bike-light']").click()

    # Cek counter cart
    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("2")

    # Masuk ke cart
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".cart_item")).to_have_count(2)
