from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from axe_selenium_python import Axe
import os
import json

def test_form():
    # Load form definitions
    form_path = os.path.join(os.path.dirname(__file__), '../form definitions/example_form.json')
    with open(form_path, 'r') as f:
        form_data = json.load(f)

    # Setup Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Open the target form URL
        driver.get(form_data['url'])

        # Fill in form fields
        for field in form_data['fields']:
            element = driver.find_element(By.NAME, field['name'])
            element.send_keys(field['value'])

        # Submit the form
        driver.find_element(By.XPATH, form_data['submit_button']).click()

        # Add verification logic here
        print("Form submitted successfully")

        # Perform accessibility checks using Axe
        axe = Axe(driver)
        axe.inject()  # Inject the axe script into the page

        # Run Axe accessibility checks
        results = axe.run()

        # Save accessibility report to a JSON file
        axe.write_results(results, 'accessibility_report.json')
        print("Accessibility report generated successfully")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_form()
