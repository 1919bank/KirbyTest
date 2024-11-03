# KirbyTest

KirbyTest is an innovative and user-friendly QA tool designed to automate the testing and validation of web forms. Inspired by the playful spirit of Kirby, this tool aims to simplify the process of ensuring form functionality, usability, and accessibility across various platforms. Whether you're a developer or a tester, KirbyTest empowers you to launch forms that work flawlessly while providing a delightful user experience.

## Features

- **Automated Testing**: Define forms using simple JSON or YAML configurations and automate the testing process. KirbyTest simulates user inputs and validates responses against expected outcomes to ensure your forms behave as intended.

- **Scalability**: Built on asynchronous programming, KirbyTest can handle multiple simultaneous form submissions, making it ideal for high-traffic applications and real-world testing scenarios.

- **Comprehensive Reporting**: Generate detailed reports that highlight test results, including success rates, error messages, and logs for each test run. Quickly identify and address issues to maintain form integrity.

- **Integration Ready**: Easily integrate KirbyTest into your CI/CD pipeline, ensuring that your forms are continually tested with every deployment or code change.

- **Cross-Browser Testing**: Leverage tools like Selenium to verify form functionality across various browsers and devices, ensuring a consistent user experience for all users.

- **Accessibility Compliance**: Automatically check your forms against accessibility standards to ensure they are usable by everyone, including those with disabilities.

- **Interactive Dashboard**: Monitor real-time performance and visualize trends over time through an intuitive web-based dashboard, making it easy to track the health of your forms.

## Installation

### Prerequisites
- Python 3.13
- ChromeDriver (or other WebDriver compatible with your browser)
- Node.js (for additional tools if needed)

### Setting Up the Environment
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/KirbyTest.git
   ```
2. Navigate to the project directory:
   ```sh
   cd KirbyTest
   ```
3. Create a virtual environment and activate it:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### WebDriver Setup
Ensure that you have the appropriate WebDriver installed (e.g., ChromeDriver). You can use `webdriver-manager` to automatically manage the driver:

```sh
pip install webdriver-manager
```

## Usage

### Running Tests
1. **Form Definition**: Define the forms you want to test using a JSON file. For example, create `form_definitions/example_form.json` with the following content:
   ```json
   {
       "url": "http://example.com/form",
       "fields": [
           {"name": "username", "value": "testuser"},
           {"name": "email", "value": "testuser@example.com"}
       ],
       "submit_button": "//button[@type='submit']"
   }
   ```

2. **Run the Form Tester**:
   ```sh
   python src/form_tester.py
   ```

3. **Generate Reports**: After running the tests, generate reports using:
   ```sh
   python src/reporter.py
   ```

### Running Tests with Pytest
KirbyTest uses `pytest` for testing. To run all tests, use:

```sh
pytest test/
```

To generate an HTML report:

```sh
pytest --html=report.html
```

## Integration with CI/CD
To integrate KirbyTest into your CI/CD pipeline, add a GitHub Actions workflow file (`.github/workflows/test.yml`):

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.13'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: pytest --html=report.html
      - name: Upload Test Report
        if: always()
        uses: actions/upload-artifact@v2
        with:
          name: test-report
          path: report.html
```

## Contributing
We welcome contributions! Please follow these steps to contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or issues, please open an issue in the GitHub repository or reach out to [your-email@example.com].

