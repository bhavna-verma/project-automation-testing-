#entertainment test case with valid element attribute
#test case will play a video
#this test case is just for entertainmenet purpose

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class entertainment():

    def test_entertainment(self):
        baseURL = "http://bhavna.42web.io/home.php"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        element = driver.find_element(By.ID, "ent")
        element.click()
        time.sleep(2)
        
        video = driver.find_element(By.ID, "song")
        video.click()

        time.sleep(5)

        
ff = entertainment()
ff.test_entertainment()
