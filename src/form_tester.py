import os
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        try:
            # Wait for the element to be visible
            element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, field['name']))
            )

            # Scroll into view before interacting
            driver.execute_script("arguments[0].scrollIntoView();", element)
            element.send_keys(field['value'])
        except TimeoutException:
            print(f"Timeout: Could not locate element with name '{field['name']}'")
            return "Failure"

    # Submit the form using the provided button selector
    try:
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, form_data['submit_button']))
        )
        submit_button.click()
    except TimeoutException:
        print("Timeout: Could not locate submit button")
        return "Failure"

    # Return success message for further testing validation
    return "Success"
