from selenium.webdriver.common.by import By
import time 

class EmployeeListPage:
    
    EMP_NAME_FILTER = (By.XPATH, "//label[text()='Employee Name']/../following-sibling::div//input")
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")
    EMP_ROWS = (By.XPATH, "//div[@role='rowgroup']/div") 
    EMP_LIST_BUTTON = (By.XPATH, "//a[text()='Employee List']")

    def __init__(self, driver):
        self.driver = driver

    def verify_employees(self, employees):
        for first_name, last_name in employees:
            
            emp_name_filter_field = self.driver.find_element(*self.EMP_NAME_FILTER)
            emp_name_filter_field.clear() 
            emp_name_filter_field.send_keys(first_name)
            self.driver.find_element(*self.SEARCH_BUTTON).click()
            time.sleep(2) 

            rows = self.driver.find_elements(*self.EMP_ROWS)
            found = False
            full_name = f"{first_name} {last_name}"
            
            
            assert len(rows) > 0, f"No employee rows found after searching for {first_name}"
            
            for row in rows:
                row_text = row.text
                if first_name in row_text and last_name in row_text:
                    
                    assert first_name in row_text, f"First name '{first_name}' not found in row"
                    assert last_name in row_text, f"Last name '{last_name}' not found in row"
                    print(f"Name Verified: {full_name}")
                    found = True
                    break
            
           
            assert found, f"Employee not found for the: {full_name}"
           
            time.sleep(2) 
            self.driver.find_element(*self.EMP_LIST_BUTTON).click()