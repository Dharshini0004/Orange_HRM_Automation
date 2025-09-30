# tests/test_login_flow.py


from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.PIMPage import PIMPage
from pages.EmployeeListPage import EmployeeListPage

# Pytest test file convention: functions must start with 'test_'
def test_orange_hrm_login_flow(setup_driver):
    
    driver = setup_driver 
    employees = [
        ["Wednesday", "Addams"],
        ["Peter", "Parker"],
        ["Tom", "Holland"]
    ]

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    pim = PIMPage(driver)
    emp_list = EmployeeListPage(driver)

    
    print("Starting Login...")
    login.login("Admin", "admin123")
    
    
    print("Navigating to PIM...")
    dashboard.go_to_pim_page()
    
    print("Adding Employees...")
    pim.add_employees(employees) 
    
    print("Navigating to Employee List for verification...")
    pim.go_to_employee_list()     
    
    print("Verifying Employees...")
    emp_list.verify_employees(employees)
    
    print("Logging out...")
    dashboard.logout()
    print("Test flow completed successfully.")

    
