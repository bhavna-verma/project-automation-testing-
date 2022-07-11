#delete test case with invalid input
#test case will fail
#message-Cannot locate option with value: 12

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class delete():

    def test_invalid_delete(self):
        baseURL = "http://bhavna.42web.io/home.php"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

       
        element = driver.find_element(By.ID, "delete_user")
        element.click()
        time.sleep(2)
 


        element=driver.find_element(By.NAME, "idnum")
        sel=Select(element)

        sel.select_by_value("12")
        print("Select 12 by value")
        time.sleep(2)

        
        submitButton = driver.find_element(By.NAME, "submit")
        submitButton.click()
        time.sleep(2)

        

ff = delete()
ff.test_invalid_delete()

