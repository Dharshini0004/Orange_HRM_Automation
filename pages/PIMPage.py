
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

class PIMPage:
    
    ADD_EMPLOYEE_BUTTON = (By.XPATH, "//a[text()='Add Employee']")
    FIRST_NAME_FIELD = (By.NAME, "firstName")
    LAST_NAME_FIELD = (By.NAME, "lastName")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    EMP_LIST_BUTTON = (By.XPATH, "//a[text()='Employee List']")
    EMP_ID_INPUT = (By.XPATH, "//label[text()='Employee Id']/../following-sibling::div/input")
    
    def __init__(self, driver):
        self.driver = driver
       
        from pages.DashboardPage import DashboardPage 
        self.dashboard = DashboardPage(driver)

    def add_employee(self, f_name, l_name):
        self.driver.find_element(*self.ADD_EMPLOYEE_BUTTON).click()
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(f_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(l_name)
        
        emp_id_field = self.driver.find_element(*self.EMP_ID_INPUT)
        existing_id = emp_id_field.get_attribute("value")
        
        try:
            new_id = int(existing_id) + 1
        except ValueError:
            new_id = 1 

        emp_id_field.click()
        
        emp_id_field.send_keys(Keys.CONTROL + 'a') 
        emp_id_field.send_keys(Keys.BACKSPACE)
        
        emp_id_field.send_keys("0" + str(new_id))
        
        self.driver.find_element(*self.SAVE_BUTTON).click()

    def add_employees(self, employees):
        for first_name, last_name in employees:
            self.add_employee(first_name, last_name)
            time.sleep(2) 
            self.dashboard.go_to_pim_page()

    def go_to_employee_list(self):
        self.driver.find_element(*self.EMP_LIST_BUTTON).click()