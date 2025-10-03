# Automation Testing Portfolio

Welcome to my **Automation Testing Portfolio** 
This repository showcases various end-to-end automated testing projects that I’ve built using **Python, Pytest, Playwright, and API testing tools**.  

The goal of this portfolio is to demonstrate my ability to:
- Design and automate **realistic business scenarios** (UI & API).
- Cover both **positive and negative test cases**.
- Generate **professional reports** for stakeholders.
- Integrate with **CI/CD pipelines** (GitHub Actions).
- Apply **Page Object Model (POM)** for scalability.

---

## Projects Included

### [SauceDemo UI Tests](./saucedemo-tests)
Automation for [SauceDemo](https://www.saucedemo.com/), a sample e-commerce site.  
**Highlights:**
- Login (success & failure)
- Add to Cart & Checkout
- Negative cases: locked user, missing fields
- HTML Reports via pytest-html
- Ready-to-use GitHub Actions workflow

---

### 📑 (Coming Soon) Restful Booker API Tests
Automation for [Restful Booker](https://restful-booker.herokuapp.com/), a sample booking API.  
**Planned Coverage:**
- Create Booking (POST)
- Retrieve Booking (GET)
- Update Booking (PUT/PATCH)
- Delete Booking (DELETE)
- Negative cases: invalid token, missing fields

---

### (Coming Soon) DemoQA Functional UI Tests
Automation for [DemoQA](https://demoqa.com/).  
**Planned Coverage:**
- Form submission & validation
- File upload & download
- Dynamic tables & CRUD actions
- Alerts, frames, and modal dialogs

---

### (Coming Soon) Cura Healthcare Appointment
Automation for [Cura Healthcare Demo](https://katalon-demo-cura.herokuapp.com/).  
**Planned Coverage:**
- Login
- Appointment booking
- Appointment history validation
- Negative cases: login failure, missing date

---

## Tech Stack
- **Language:** Python 3.10+
- **Framework:** Playwright, Pytest
- **Reporting:** pytest-html, Allure (future plan)
- **CI/CD:** GitHub Actions
- **Pattern:** Page Object Model

---

## How to Run (General)
Each project has its own folder with detailed README.  
General setup:
```bash
git clone https://github.com/renfinity88/automation-portfolio.git
cd automation-portfolio/<project-folder>
py -m venv .venv
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
playwright install
pytest -q --html=reports/report.html --self-contained-html
