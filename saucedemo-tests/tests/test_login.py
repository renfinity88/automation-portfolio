from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_success(page: Page, base_url: str):
    lp = LoginPage(page)
    inv = InventoryPage(page)

    lp.goto(base_url)
    lp.login("standard_user", "secret_sauce")
    inv.assert_logged_in()

def test_login_invalid_password(page: Page, base_url: str):
    lp = LoginPage(page)
    lp.goto(base_url)
    lp.login("standard_user", "wrong_password")
    expect(lp.error).to_be_visible()
    expect(lp.error).to_contain_text("Username and password do not match")
