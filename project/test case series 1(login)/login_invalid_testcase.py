#login test case with invalid input
#test case will execute but will not login
#test case with in valid usernamee and passworde

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginTests():

    def test_invalidLogin(self):
        baseURL = "http://bhavna.42web.io/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)


        emailField = driver.find_element(By.ID, "username")
        emailField.send_keys("xyz")

        passwordField = driver.find_element(By.NAME, "password")
        passwordField.send_keys("xyz")

        time.sleep(2)

        loginButton = driver.find_element(By.ID, "submit")
        loginButton.click()
        time.sleep(2)


        
ff = LoginTests()
ff.test_invalidLogin()
