#view all user data test case with valid URL
#test case will execute successfully without any error


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class view_alldata():

    def test_view_alldata(self):
        baseURL = "http://bhavna.42web.io/home.php"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        time.sleep(2)

        element = driver.find_element(By.ID, "all_user")
        element.click()
        time.sleep(2)


        time.sleep(3)


ff = view_alldata()
ff.test_view_alldata()
