# SauceDemo UI Automation Testing

Automated end-to-end tests for [SauceDemo](https://www.saucedemo.com/) using **Python, Pytest, and Playwright**.  
This project is part of my automation testing portfolio, showcasing both **positive** and **negative** scenarios, CI/CD readiness, and structured reporting.

---

## Tech Stack
- **Language:** Python 3.10+
- **Test Runner:** Pytest
- **Framework:** Playwright
- **Reports:** pytest-html
- **Design Pattern:** Page Object Model (for login & inventory pages)
- **CI/CD:** GitHub Actions (ready to integrate)

---

## Test Scenarios

### Positive Test Cases
- **Login Success** → valid user can log in.  
- **Add to Cart** → add multiple products, validate cart badge & items.  
- **Checkout** → complete checkout flow and verify success message.  
- **Checkout Extended** → verify Payment Info, Shipping Info, Price Total, Subtotal, Tax, and Total.  

### Negative Test Cases
- **Invalid Login** → wrong password shows error.  
- **Locked Out User** → locked user cannot log in.  
- **Checkout Missing First Name** → error: *First Name is required*.  
- **Checkout Missing Last Name** → error: *Last Name is required*.  
- **Checkout Missing Postal Code** → error: *Postal Code is required*.  

---

## Project Structure
saucedemo-tests/
├── pages/
│ ├── login_page.py
│ └── inventory_page.py
├── tests/
│ ├── test_login.py
│ ├── test_cart.py
│ ├── test_checkout.py
│ ├── test_checkout_extended.py
│ └── test_negative_checkout.py
├── reports/
├── conftest.py
├── requirements.txt
└── README.md

yaml
Copy code

---

## How to Run Tests

1. **Clone repo & enter project**
   ```bash
   git clone https://github.com/<your-username>/automation-portfolio.git
   cd automation-portfolio/saucedemo-tests
Create virtual environment

bash
Copy code
py -m venv .venv
.venv\Scripts\activate     # Windows
# source .venv/bin/activate   # Mac/Linux
Install dependencies

bash
Copy code
pip install -r requirements.txt
playwright install
Run all tests (headless)

bash
Copy code
pytest -q
Run all tests with browser visible

bash
Copy code
pytest -q --headed --slowmo 200
Generate HTML Report

bash
Copy code
pytest -q --html=reports/report.html --self-contained-html
Open reports/report.html in your browser.

