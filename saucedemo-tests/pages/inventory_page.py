from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")

    def assert_logged_in(self):
        expect(self.title).to_have_text("Products")
