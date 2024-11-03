import os
from jinja2 import Template

def generate_report(data):
    # Get the absolute path to report_template.html
    template_path = os.path.join(os.path.dirname(__file__), '../report.html')

    # Alternatively, if it's in a 'templates' directory, update the path accordingly:
    # template_path = os.path.join(os.path.dirname(__file__), '../templates/report.html')

    # Load the template
    with open(template_path, 'r') as template_file:
        template = Template(template_file.read())

    # Render the template with data
    report = template.render(data=data)

    # Write the rendered report to an HTML file
    with open("report.html", "w") as f:
        f.write(report)

# Example usage:
if __name__ == "__main__":
    data = {'form_name': 'Contact Us', 'status': 'Success', 'errors': []}
    generate_report(data)
