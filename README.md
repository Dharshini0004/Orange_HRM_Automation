# OrangeHRM Web Automation Project

## 1. Overview 

This project is an automation framework built using **Python**, the **Pytest** testing framework, **Selenium WebDriver**, and the **Page Object Model (POM)** design pattern. It automates critical user workflows in the [OrangeHRM Demo Application](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login).

The framework demonstrates the best practices for modern Python test automation, focusing on:
* Clean, scalable structure using POM.
* **Fixtures** (`conftest.py`) for efficient setup and teardown.
* Reliable assertions and validations for functional correctness.


## 2. Technology Stack

| Component        | Technology           | Role                                         |
| :--------------: | :------------------:| :-------------------------------------------- |
| **Language**     | Python 3.8+          | Primary development language                  |
| **Framework**    | Pytest               | Test execution, organization, and reporting   |
| **Automation**   | Selenium WebDriver   | Browser control and interaction               |
| **Driver Mgt.**  | webdriver-manager    | Automated driver installation (e.g., ChromeDriver) |
| **Design**       | Page Object Model    | Design pattern for reusability and maintenance |

---

## 3. Automated Workflows 

The automation suite covers the following comprehensive user journey within the OrangeHRM application:

1.  **Login Flow:**
    * Uses provided demo credentials (`Admin`, `admin123`).
    * Validates successful navigation to the Dashboard after authentication.

2.  **PIM Module Navigation:**
    * Navigates to the **PIM (Personnel Information Management)** module from the Dashboard menu.

3.  **Add Employees (Data-Driven):**
    * Adds multiple employees based on a data-driven approach (using a list of names).
    * Includes logic to handle and dynamically adjust the Employee IDs for uniqueness during creation.
    * **Edge Case Handled:** During employee creation (`PIMPage.py`), the script addresses the potential for duplicate employee IDs by extracting the existing default ID, incrementing its numeric value, and re-entering the unique ID. This ensures reliable employee creation.


4.  **Verify Employees:**
    * Navigates to the *Employee List* page.
    * Searches for the newly added employees using the Employee Name filter.
    * Validates the reliable presence of the employee's first and last names in the result table.

5.  **Logout:**
    * Successfully logs out from the application, returning to the Login page.

---

## 4. Project Structure 

The Pytest-based structure ensures logical separation of setup, page logic, and test cases:

orangehrm-pytest/
├── conftest.py             # Pytest Fixtures (WebDriver setup/ logic)
├── pages/                  # Page Object Model (POM) classes
│   ├── LoginPage.py
│   ├── DashboardPage.py
│   ├── PIMPage.py
│   └── EmployeeListPage.py
├── tests/                  # Pytest Test Case files
│   └── TC_Login_flow.py  # Primary test scenario execution
└── README.md
---

### 5. Setup and Execution 

### A. Prerequisites
Make sure the following are installed on your system:

- **Python 3.8+**
- **Git**
- **Google Chrome Browser**

---

### B. Installation Steps

#### 1. Clone the Repository
### Bash
git clone [Your Repository URL Here]
cd [Your Project Folder Name]

#### 2. Create the Virtual Environment:
Create an isolated environment named venv to house the project's dependencies.

Bash

# Use 'python' first, but if that fails, use 'py'
python -m venv venv
# OR
py -m venv venv
Activate the Environment:
You must activate the environment every time you start a new terminal session.

Operating System	           Command to Use
Windows (PowerShell)	        .\venv\Scripts\activate
Windows (Command Prompt / CMD)	.\venv\Scripts\activate.bat
macOS / Linux	                 source venv/bin/activate

#### 3. Install Dependencies:
With the virtual environment active, install all necessary packages (selenium, pytest, webdriver-manager):

### Bash
pip install selenium pytest webdriver-manager