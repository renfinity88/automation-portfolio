from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login-button")
        self.error = page.locator("[data-test='error']")

    def goto(self, base_url: str):
        self.page.goto(base_url)

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()
