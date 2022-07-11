#login test case with valid input
#test case will execute successfully without any error
#all the user in "click to view all user data " can login with there usernamee and passworde

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginTests():

    def test_validLogin(self):
        baseURL = "http://bhavna.42web.io/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)


        emailField = driver.find_element(By.ID, "username")
        emailField.send_keys("bhavna123")

        passwordField = driver.find_element(By.NAME, "password")
        passwordField.send_keys("7000944541")

        time.sleep(2)

        loginButton = driver.find_element(By.ID, "submit")
        loginButton.click()
        time.sleep(2)


        
ff = LoginTests()
ff.test_validLogin()
