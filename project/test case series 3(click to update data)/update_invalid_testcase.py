#this test case will fail as no such value in dropdown exist
#message-Cannot locate option with value: 7

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class update():

    def test_invalid_update(self):
        baseURL = "http://bhavna.42web.io/home.php"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        
        element = driver.find_element(By.ID, "update_user")
        element.click()
        time.sleep(2)


        element=driver.find_element(By.NAME, "idnum")
        sel=Select(element)

        sel.select_by_value("7")
        print("select 7 by value ")
        time.sleep(2)

        submitButton = driver.find_element(By.NAME, "submit")
        submitButton.click()
        time.sleep(2)

        updatename = driver.find_element(By.ID, "upName")
        updatename.click()
        time.sleep(2)
        x=driver.find_element(By.ID,"upName")
        z=x.get_attribute('value')
        y=""
        for i in range(len(z)):
            y=y+"\b"
            
      
        updatename.send_keys(y)
        time.sleep(2)
        updatename.send_keys("bhawna")
        time.sleep(2)

        driver.execute_script("window.scrollBy(0,1000);")
        
        submit = driver.find_element(By.ID, "submit_up")
        submit.click()
        time.sleep(2)
 

ff = update()
ff.test_invalid_update()

	
