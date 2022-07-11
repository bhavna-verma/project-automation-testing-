#test case with invalid element attribute
#test case will  not execute
#message-no such element: Unable to locate element: {"method":"css selector","selector":"[id="username"]"}



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class create():

    def test_invalid_create(self):
        baseURL = "http://bhavna.42web.io/home.php"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        element = driver.find_element(By.ID, "create_user")
        element.click()
        time.sleep(2)


        name = driver.find_element(By.ID, "new_name")
        name.send_keys("mahi")

        
        username = driver.find_element(By.ID, "username")
        username.send_keys("mahi123")


        password = driver.find_element(By.ID, "new_password")
        password.send_keys("mahi@123")

        salary = driver.find_element(By.ID, "new_salary")
        salary.send_keys("350000")


        position = driver.find_element(By.ID, "new_position")
        position.send_keys("PBA")


        submitButton = driver.find_element(By.NAME, "submit")
        submitButton.click()
        time.sleep(2)

ff = create()
ff.test_invalid_create()
       
