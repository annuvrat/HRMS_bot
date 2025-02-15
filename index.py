from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Replace with actual HRMS URL
HRMS_URL = "https://hrms.stagingapps.xyz/dashboard"

# Your login credentials
EMAIL = "annuvrat.vdoit@gmail.com"
PASSWORD = ""

# Set up Chrome with auto-managed driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open in full screen

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open HRMS webpage
    driver.get(HRMS_URL)
    time.sleep(5)  # Wait for page to load

    # Find and fill in the email field
    email_input = driver.find_element(By.NAME, "email")  # Update with actual name attribute
    email_input.send_keys(EMAIL)

    # Find and fill in the password field
    password_input = driver.find_element(By.NAME, "password")  # Update with actual name attribute
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)  # Press Enter to log in

    time.sleep(10)  # Wait for login to complete

    # Click "Clock-In" button
    clock_in_button = driver.find_element(By.CLASS_NAME, "bg-indigo-600")  # Update if needed
    clock_in_button.click()

    print("Successfully clocked in. Waiting for 9 hours...")

    # Wait for 9 hours (9 * 60 * 60 seconds)
    time.sleep(9 * 60 * 60)

    # Click "Clock-Out" button
    clock_out_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Clock Out')]")
    clock_out_button.click()

    print("Successfully clocked out.")

finally:
    # Close the browser
    driver.quit()
