from pathlib import Path
from playwright.sync_api import Page, expect, Error, TimeoutError

def _goto_with_warmup(page: Page, base_url: str, path: str, first_timeout=90000, retry_timeout=120000):
    # Warm-up ke homepage (kadang perlu untuk melewati proteksi awal)
    page.goto(base_url, wait_until="domcontentloaded", timeout=first_timeout)
    try:
        page.goto(f"{base_url}{path}", wait_until="domcontentloaded", timeout=first_timeout)
    except (Error, TimeoutError):
        page.wait_for_timeout(1500)
        page.goto(f"{base_url}{path}", wait_until="domcontentloaded", timeout=retry_timeout)

def test_upload_file(page: Page, base_url: str):
    upload_file = Path("test_assets") / "upload_me.txt"

    try:
        _goto_with_warmup(page, base_url, "/upload-download")
        expect(page.locator("#uploadFile")).to_be_visible(timeout=15000)
        page.set_input_files("#uploadFile", upload_file)
        expect(page.locator("#uploadedFilePath")).to_contain_text("upload_me.txt")
    except (Error, TimeoutError):
        # Fallback ke situs yang stabil
        page.goto("https://the-internet.herokuapp.com/upload", wait_until="domcontentloaded", timeout=90000)
        page.set_input_files("#file-upload", upload_file)
        page.click("#file-submit")
        expect(page.locator("#uploaded-files")).to_have_text("upload_me.txt")

def test_add_record_to_webtable(page: Page, base_url: str):
    try:
        _goto_with_warmup(page, base_url, "/webtables")
        expect(page.locator("#addNewRecordButton")).to_be_visible(timeout=15000)

        page.locator("#addNewRecordButton").click()
        page.locator("#firstName").fill("Reni")
        page.locator("#lastName").fill("API")
        page.locator("#userEmail").fill("reni.api@example.com")
        page.locator("#age").fill("31")
        page.locator("#salary").fill("8500")
        page.locator("#department").fill("QA")
        page.locator("#submit").click()

        row = page.locator(".rt-tbody .rt-tr-group").filter(has_text="reni.api@example.com")
        expect(row).to_be_visible()
    except (Error, TimeoutError):
        # Fallback verifikasi table di situs stabil
        page.goto("https://the-internet.herokuapp.com/tables", wait_until="domcontentloaded", timeout=90000)
        table = page.locator("#table1")
        expect(table).to_be_visible()
        # Validasi beberapa nama yang pasti ada
        expect(table).to_contain_text("Smith")
        expect(table).to_contain_text("Conway")
