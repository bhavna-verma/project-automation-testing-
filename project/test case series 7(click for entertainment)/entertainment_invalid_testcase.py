#entertainment test case with invalid element attribute
#test case will not play a video
#message-Unable to locate element: {"method":"css selector","selector":"[id="id_selenium"]"}


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class entertainment():

    def test_invalid_entertainment(self):
        baseURL = "http://bhavna.42web.io/home.php"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        element = driver.find_element(By.ID, "ent")
        element.click()
        time.sleep(2)

        driver.execute_script("window.scrollBy(0,1000);") 
        
        video = driver.find_element(By.ID, "id_selenium")
        video.click()

        time.sleep(5)

        
ff = entertainment()
ff.test_invalid_entertainment()

