import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from src.form_tester import test_form

@pytest.fixture
def driver():
    # Set up the WebDriver for each test
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()  # Cleanup after each test

def test_form_submission(driver):
    # Assuming `test_form` takes driver as a parameter to simulate form filling
    assert test_form(driver) == "Success", "Form submission did not succeed"
