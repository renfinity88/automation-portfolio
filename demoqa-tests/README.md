# DemoQA UI Tests (Playwright + Pytest)

Covers:
- Practice Form end-to-end (with upload, state/city select, modal verification)
- File Upload page
- WebTables: add record & verify

## Run locally
cd demoqa-tests
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install
pytest -q --headed --slowmo 150 --html=reports/report.html --self-contained-html

vbnet
Copy code
