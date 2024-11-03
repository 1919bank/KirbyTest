import os
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def test_form(driver):
    # Load form definitions from the JSON file
    form_path = os.path.join(os.path.dirname(__file__), '../form definitions/example_form.json')

    with open(form_path, 'r') as f:
        form_data = json.load(f)

    # Open the target form URL using the WebDriver
    driver.get(form_data['url'])

    # Fill in form fields with the provided data from the JSON
    for field in form_data['fields']:
        element = driver.find_element(By.NAME, field['name'])
        element.send_keys(field['value'])

    # Submit the form using the provided button selector
    driver.find_element(By.XPATH, form_data['submit_button']).click()

    # Return success or failure message for further testing validation
    return "Success"
