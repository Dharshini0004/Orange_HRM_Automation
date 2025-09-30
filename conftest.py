# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # <--- IMPORT OPTIONS

@pytest.fixture(scope="function")
def setup_driver():
    
    
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    
    
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    driver.maximize_window()
    driver.implicitly_wait(30) 
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    yield driver
    
    driver.quit()