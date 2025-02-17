from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime


HRMS_URL = "https://hrms.stagingapps.xyz/dashboard"
EMAIL = ""
PASSWORD = ""


today = datetime.datetime.today().weekday()


if today < 5:
    def clock_in():
        """Function to clock in and close the browser."""
        driver = webdriver.Chrome()
        driver.get(HRMS_URL)
        time.sleep(10)  

        # Enter login details
        driver.find_element(By.NAME, "email").send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD, Keys.RETURN)
        time.sleep(10)  

        # Click "Clock In"
        driver.find_element(By.CLASS_NAME, "bg-indigo-600").click()
        print("Successfully clocked in.")
        time.sleep(5)  
        # Close the browser
        driver.quit()

    def clock_out():
        """Function to clock out after nine hours and close the browser."""
        driver = webdriver.Chrome()
        driver.get(HRMS_URL)
        time.sleep(10)  # Wait for page to load

        # Enter login details again
        driver.find_element(By.NAME, "email").send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD, Keys.RETURN)
        time.sleep(10)  # Wait for login to complete

        # Click "Clock Out"
        driver.find_element(By.XPATH, "//button[contains(text(), 'Clock Out')]").click()
        print("Successfully clocked out.")
        time.sleep(10)  
        # Close the browser
        driver.quit()

    # Clock in now
    clock_in()

    # Wait for nine hours (Script ends, not keeping the tab open)
    time.sleep(9 * 60 * 60)

    # Clock out after nine hours
    clock_out()
else:
    print("Today is a weekend. No need to run the script.")
