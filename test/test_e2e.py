import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from src.form_tester import test_form
from src.reporter import generate_report
from axe_selenium_python import Axe


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_full_workflow(driver):
    # Run form testing
    result = test_form(driver)

    # Run accessibility testing with Axe
    axe = Axe(driver)
    axe.inject()
    results = axe.run()

    # Verify accessibility results
    assert len(results['violations']) == 0, "Accessibility issues found"

    # Generate a report based on the form test
    data = {'form_name': 'Contact Us', 'status': result, 'errors': []}
    report = generate_report(data)

    # Ensure the report contains the correct data
    assert "Contact Us" in report
    assert "Success" in report if result == "Success" else "Failure" in report
