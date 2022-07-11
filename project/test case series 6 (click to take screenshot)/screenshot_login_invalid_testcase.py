#test case to take screenshot
#this test case will take screenshot of wrong username and pasword (login page)
#screenshot will be saved with current date and time 

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from PIL import Image
import time

class Tests():

    def test_ss(self):
        baseURL = "http://bhavna.42web.io/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H-%M-%S")



        emailField = driver.find_element(By.ID, "username")
        emailField.send_keys("Jatin")

        passwordField = driver.find_element(By.ID, "password")
        passwordField.send_keys("123")

        time.sleep(2)

        loginButton = driver.find_element(By.NAME, "submit")
        loginButton.click()

        time.sleep(5)

        driver.save_screenshot('screenshot/screenshot'+dt_string+'.png')
        screenshot = Image.open('screenshot/screenshot'+dt_string+'.png')
        screenshot.show()
        

ff = Tests()
ff.test_ss()

