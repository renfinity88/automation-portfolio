from pathlib import Path
from playwright.sync_api import Page, expect

def test_practice_form_submit_success(page: Page, base_url: str):
    page.goto(f"{base_url}/automation-practice-form")

    # Buang iklan/overlay yang kadang nutup tombol submit
    page.evaluate("document.querySelector('#fixedban')?.remove()")
    page.evaluate("document.querySelector('#RightSide_Advertisement')?.remove()")

    # Isi form
    page.locator("#firstName").fill("Reni")
    page.locator("#lastName").fill("Tester")
    page.locator("#userEmail").fill("reni.tester@example.com")
    page.locator("label[for='gender-radio-2']").click()  # Female
    page.locator("#userNumber").fill("0812345678")

    # Date of Birth (ketik langsung agar stabil)
    dob = page.locator("#dateOfBirthInput")
    dob.click()
    dob.press("Control+a")
    dob.type("10 Oct 1990")
    dob.press("Enter")

    # Subjects (auto-complete)
    subj = page.locator("#subjectsInput")
    subj.type("English")
    subj.press("Enter")

    # Hobbies
    page.locator("label[for='hobbies-checkbox-1']").click()  # Sports

    # Upload file
    page.set_input_files("#uploadPicture", Path("demoqa-tests/test_assets/upload_me.txt"))

    # Address
    page.locator("#currentAddress").fill("Jl. Automation No. 88, Surabaya")

    # State/City (react-select)
    page.locator("#state").click()
    page.locator("#react-select-3-input").type("NCR")
    page.locator("#react-select-3-input").press("Enter")
    page.locator("#city").click()
    page.locator("#react-select-4-input").type("Delhi")
    page.locator("#react-select-4-input").press("Enter")

    # Submit
    page.locator("#submit").click()

    # Verifikasi modal muncul & isinya benar
    expect(page.locator("#example-modal-sizes-title-lg")).to_have_text("Thanks for submitting the form")
    modal = page.locator(".modal-content .table-responsive")
    expect(modal).to_contain_text("Reni Tester")
    expect(modal).to_contain_text("reni.tester@example.com")
    expect(modal).to_contain_text("Female")
    expect(modal).to_contain_text("NCR Delhi")

    # Tutup modal
    page.locator("#closeLargeModal").click()
