from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open('report.json') as f:
        report_data = json.load(f)
    return render_template('dashboard.html', data=report_data)

if __name__ == "__main__":
    app.run(debug=True)
