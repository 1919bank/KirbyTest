import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.form_tester import test_form
from src.reporter import generate_report

def test_form_and_report(driver):
    result = test_form(driver)
    data = {'form_name': 'Contact Us', 'status': result, 'errors': []}
    report = generate_report(data)

    # Verify that the generated report reflects the form submission result
    assert "Contact Us" in report
    assert "Success" in report if result == "Success" else "Failure" in report
