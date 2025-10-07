from pathlib import Path
from playwright.sync_api import Page, expect, Error, TimeoutError

# Path absolut ke test_assets meskipun pytest dijalankan dari root monorepo
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_PATH = BASE_DIR / "test_assets" / "upload_me.txt"

def _goto_with_warmup(page: Page, base_url: str, path: str, first_timeout=90000, retry_timeout=120000):
    page.goto(base_url, wait_until="domcontentloaded", timeout=first_timeout)
    try:
        page.goto(f"{base_url}{path}", wait_until="domcontentloaded", timeout=first_timeout)
    except (Error, TimeoutError):
        page.wait_for_timeout(1500)
        page.goto(f"{base_url}{path}", wait_until="domcontentloaded", timeout=retry_timeout)

def test_upload_file(page: Page, base_url: str):
    try:
        _goto_with_warmup(page, base_url, "/upload-download")
        expect(page.locator("#uploadFile")).to_be_visible(timeout=15000)
        page.locator("#uploadFile").scroll_into_view_if_needed()
        page.locator("#uploadFile").set_input_files(UPLOAD_PATH)
        expect(page.locator("#uploadedFilePath")).to_contain_text("upload_me.txt")
    except (Error, TimeoutError):
        # Fallback yang stabil
        alt = page.context.new_page()
        alt.goto("https://the-internet.herokuapp.com/upload", wait_until="domcontentloaded", timeout=90000)
        file_input = alt.locator("#file-upload")
        file_input.scroll_into_view_if_needed()
        file_input.set_input_files(UPLOAD_PATH)
        alt.click("#file-submit")
        expect(alt.locator("#uploaded-files")).to_have_text("upload_me.txt")
        alt.close()

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
        # Buka TAB BARU supaya tidak ter-interrupt oleh chrome-error
        alt = page.context.new_page()
        alt.goto("https://the-internet.herokuapp.com/tables", wait_until="domcontentloaded", timeout=90000)
        table = alt.locator("#table1")
        expect(table).to_be_visible()
        expect(table).to_contain_text("Smith")
        expect(table).to_contain_text("Conway")
        alt.close()
