import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

class TestAbs(unittest.TestCase):

    def test_link1(self):
        browser = webdriver.Chrome()
        browser.get(link1)
        first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your first name']")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your last name']")
        last_name.send_keys("Petrov")
        email = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your email']")
        email.send_keys("Test@test.com")
        phone = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your phone:']")
        phone.send_keys("89999999999")
        address = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your address:']")
        address.send_keys("moscow")
        button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        button.click()

    def test_link2(self):
        browser = webdriver.Chrome()
        browser.get(link2)
        first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your first name']")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your last name']")
        last_name.send_keys("Petrov")
        email = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your email']")
        email.send_keys("Test@test.com")
        phone = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your phone:']")
        phone.send_keys("89999999999")
        address = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your address:']")
        address.send_keys("moscow")
        button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        button.click()


if __name__ == "__main__":
    unittest.main()