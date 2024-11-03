import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.reporter import generate_report

def test_generate_report():
    data = {'form_name': 'Contact Us', 'status': 'Success', 'errors': []}
    report = generate_report(data)

    # Assert that certain elements are present in the generated report
    assert "<title>Report</title>" in report
    assert "Contact Us" in report
    assert "Success" in report
