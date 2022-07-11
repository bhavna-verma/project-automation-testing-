#test case to take screenshot of "click to take screenshot" option
#screenshot will be saved with current date and time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from PIL import Image

class Tests():

    def test_home_ss(self):
        baseURL = "http://bhavna.42web.io/home.php"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H-%M-%S")


        ss = driver.find_element(By.ID, "screenshot")
        ss.click()
        time.sleep(2)

        ss_take = driver.find_element(By.ID, "photo")
        ss_take.click()
        time.sleep(2)

        

        
        driver.save_screenshot('screenshot/screenshot'+dt_string+'.png')
        screenshot = Image.open('screenshot/screenshot'+dt_string+'.png')
        screenshot.show()
        

        

ff = Tests()
ff.test_home_ss()

