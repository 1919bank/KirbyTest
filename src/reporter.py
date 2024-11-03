import os
from jinja2 import Template

def generate_report(data):
    # Correct path for the template file
    template_path = os.path.join(os.path.dirname(__file__), '../templates/report_template.html')

    # Load and render the template with data
    if not os.path.exists(template_path):
        print(f"Error: Template file not found at {template_path}")
        return None

    with open(template_path, 'r') as template_file:
        template = Template(template_file.read())
        report = template.render(data=data)

    # Save the generated report to a file
    report_path = os.path.join(os.path.dirname(__file__), '../report.html')
    with open(report_path, 'w') as f:
        f.write(report)

    return report
