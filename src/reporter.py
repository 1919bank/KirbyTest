import os
from jinja2 import Template

def generate_report(data):
    # Correct path for the template file
    template_path = os.path.join(os.path.dirname(__file__), '../report_template.html')

    # Load and render the template with data
    with open(template_path, 'r') as template_file:
        template = Template(template_file.read())

    report = template.render(data=data)

    # Write the rendered report to an HTML file
    with open("report.html", "w") as f:
        f.write(report)

    return report  # Return the report so it can be used in tests

# Example usage:
if __name__ == "__main__":
    data = {'form_name': 'Contact Us', 'status': 'Success', 'errors': []}
    generate_report(data)

