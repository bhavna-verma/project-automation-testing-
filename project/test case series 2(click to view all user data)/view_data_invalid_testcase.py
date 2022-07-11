#view all user data test case with invalid ID
#test case will not execute
#Message: no such element: Unable to locate element: {"method":"css selector","selector":"[id="alll_user"]"}


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

        time.sleep(3)

        element = driver.find_element(By.ID, "alll_user")
        element.click()
        time.sleep(2)



ff = view_alldata()
ff.test_view_alldata()
