from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    try:
        with open("object_log.json", "r") as json_file:
            data = json.load(json_file)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        data = []

    # Check if data is a list
    if not isinstance(data, list):
        # Set data to a default value that the template is expecting
        data = [{"class": "No data available"}]

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
