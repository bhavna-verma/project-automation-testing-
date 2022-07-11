#login test case with valid input
#test case will execute successfully without any error
#for security purpose the login page is created in a way that apart from user if someone else will try to login with a specific password "'or'1'='1" they will be able to login successfully
#sometime hackers can hack without password or just by using username for this here is a login page which will login only with specfic password and with any username
# ('or'1'='1) password is difficult to guess for hacker

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
        emailField.send_keys("xyz")

        passwordField = driver.find_element(By.NAME, "password")
        passwordField.send_keys("'or'1'='1")

        time.sleep(2)

        loginButton = driver.find_element(By.ID, "submit")
        loginButton.click()
        time.sleep(2)


        
ff = LoginTests()
ff.test_validLogin()
