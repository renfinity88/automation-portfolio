from pathlib import Path
from playwright.sync_api import Page, expect

def test_upload_file(page: Page, base_url: str):
    page.goto(f"{base_url}/upload-download")
    page.set_input_files("#uploadFile", Path("demoqa-tests/test_assets/upload_me.txt"))
    # DemoQA menampilkan "C:\\fakepath\\upload_me.txt"
    expect(page.locator("#uploadedFilePath")).to_contain_text("upload_me.txt")

def test_add_record_to_webtable(page: Page, base_url: str):
    page.goto(f"{base_url}/webtables")

    page.locator("#addNewRecordButton").click()
    page.locator("#firstName").fill("Reni")
    page.locator("#lastName").fill("API")
    page.locator("#userEmail").fill("reni.api@example.com")
    page.locator("#age").fill("31")
    page.locator("#salary").fill("8500")
    page.locator("#department").fill("QA")
    page.locator("#submit").click()

    # Cari row yang mengandung email tersebut
    row = page.locator(".rt-tbody .rt-tr-group").filter(has_text="reni.api@example.com")
    expect(row).to_be_visible()
