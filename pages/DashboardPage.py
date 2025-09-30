from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class DashboardPage:
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    PROFILE_MENU = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def go_to_pim_page(self):
        pim_element = self.driver.find_element(*self.PIM_MENU)
        ActionChains(self.driver).move_to_element(pim_element).click().perform()

    def logout(self):
        self.driver.find_element(*self.PROFILE_MENU).click()
        self.driver.find_element(*self.LOGOUT_BUTTON).click()