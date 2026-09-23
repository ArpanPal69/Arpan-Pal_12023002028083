# 🚀 Enterprise API Automation Framework (Python + BDD)

**Capstone Assignment 3: Python API Automation Framework with Requests + Behave BDD**

---

## 👨‍💻 Developer Profile
| Field | Details |
| :--- | :--- |
| **Name** | Arpan Pal |
| **College** | Institute of Engineering and Management, Kolkata |
| **Department** | CSE (AI & ML) |
| **Enrollment No.** | 12023002028083 |
| **Registration No.** | 304202300901001 |
| **Email (Personal)** | arpanpalbwn@gmail.com |
| **Email (Institutional)** | arpan.pal2023@iem.edu.in |

---

## 🎥 Project Demonstration Video
**Watch the full project walkthrough and execution here:**  
[Project Demonstration Video](https://drive.google.com/file/d/1Y-3An79GkAZI0eFpdlAKFvjUIQ71uanw/view?usp=sharing)

---

## 🎯 Objective
To build a complete, scalable, and reusable API Automation Framework from scratch targeting the User Management API (`https://jsonplaceholder.typicode.com/`). The framework is engineered to industry standards, utilizing Python Requests, REST API Testing methodologies, Authentication simulation, the Behave BDD Framework, and dynamic Allure Reporting.

## 🛑 Problem Statement
In enterprise software engineering, standard basic API automation scripts suffer from four major architectural flaws:
1. **Massive Security Risks:** Beginners hardcode sensitive data (URLs, Auth Tokens) into source code. If pushed to GitHub, this compromises company servers.
2. **Poor Performance:** Basic tests open a brand new HTTP/TCP connection for every single request, wasting server resources and causing network latency.
3. **Zero Traceability:** When tests run overnight on a CI/CD server and fail, developers are left with a "black box" and must guess what payload caused the crash.
4. **Lack of Stakeholder Visibility:** Automation code is highly technical. Non-technical Product Owners and Business Analysts cannot read Python to verify if business requirements are met.

## 🧠 Methodology & Architectural Solutions
To solve these problems, this framework implements the following enterprise-grade solutions:

* **Security via `.env` Vault:** Implemented `python-dotenv` and `.gitignore`. Sensitive credentials and URLs are stored strictly in local memory and injected dynamically, ensuring zero secrets leak to version control.
* **Speed via Connection Pooling:** Built a custom `APIClient` class utilizing `requests.Session()`. This reuses a single TCP network tunnel for the entire test suite, reducing execution time to ~1-2 seconds.
* **Elite Traceability via Allure Hooks:** Engineered a custom `_log_to_allure()` method. The framework actively intercepts live network traffic and attaches the raw JSON Request Payloads and Response Bodies directly to the HTML report.
* **Agile Alignment via BDD (Behave):** Abstracted complex Python network logic behind plain English `Given/When/Then` Gherkin feature files, allowing non-technical managers to verify product health.

### 🌟 Advanced Enterprise Enhancements (Senior-Level Upgrades)
Beyond the core requirements, this framework includes 5 advanced architectural upgrades:
1. **Dynamic Runtime Authentication:** Framework can dynamically fetch fresh JWT tokens during the `before_all` execution phase.
2. **Cross-Environment Execution:** Configured Behave's `-D BASE_URL` flag to allow CI/CD pipelines to run tests against DEV, QA, or PROD environments dynamically from the terminal.
3. **Dynamic Data Generation:** Integrated the Python `Faker` library to generate 100% unique, randomized payloads (Names, Emails) to prevent unique-constraint database collisions.
4. **API Contract Validation:** Implemented `jsonschema` validation to strictly verify the structural blueprint and data types of the API responses.
5. **Automated State Teardown:** Built an `after_scenario` hook that actively sends a `DELETE` request to clean up any test data generated during the run, maintaining database hygiene.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **API Engine:** `requests`
* **BDD Framework:** `behave`
* **Reporting:** `allure-behave`
* **Security:** `python-dotenv`
* **Data Generation:** `faker`
* **Contract Testing:** `jsonschema`

---

## 📂 File Structure
```text
Capstone Project/
├── features/
│   ├── environment.py              # Setup (Env Loader) and Teardown Hooks
│   ├── users_api.feature           # Plain English BDD Test Scenarios
│   └── steps/
│       └── api_steps.py            # Python Glue Code & Schema Assertions
├── utils/
│   ├── api_client.py               # Core Network Engine (requests.Session)
│   ├── payloads.py                 # Dynamic Test Data Generator (Faker)
│   └── schemas.py                  # Strict API Contract Blueprints
├── .env                            # Local Security Vault (Ignored by Git)
├── .gitignore                      # Git Exclusion Rules
├── behave.ini                      # Behave & Allure Formatter Configuration
├── categories.json                 # Custom Allure Defect Routing Rules
├── requirements.txt                # Python Dependencies List
└── README.md                       # Project Documentation
```

---

## 🚀 Execution & Installation Guide

### 1. Setup Virtual Environment
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Reporting Directories
```cmd
mkdir allure-results
echo Base_URL=https://jsonplaceholder.typicode.com > allure-results\environment.properties
echo OS=Windows 10 >> allure-results\environment.properties
echo Environment=QA_Testing >> allure-results\environment.properties
copy categories.json allure-results\categories.json
```

### 3. Execute Tests & Generate Reports
```cmd
behave
allure generate allure-results -o allure-report --clean
xcopy "allure-report\history" "allure-results\history\" /E /I /Y
behave
allure serve allure-results
```

---

## 📊 Results Achieved
* **100% Test Pass Rate:** Successfully automated and validated both `GET` and `POST` endpoints.
* **Zero Hardcoded Secrets:** Framework achieves full enterprise security compliance.
* **Historical CI/CD Tracking:** The dashboard successfully visualizes performance trends, network duration speeds, and defect categorizations over multiple test runs.

## 🏁 Conclusion
This project successfully bridges the gap between highly technical API network validation and business-friendly Agile reporting. By incorporating Connection Pooling, JSON Schema Validation, and Dynamic Data Generation, this architecture operates securely and efficiently at an industrial standard, fully satisfying all Capstone requirements.
