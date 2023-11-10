from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    try:
        with open("object_log.json", "r") as json_file:
            data = [json.loads(line) for line in json_file]
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        data = []

    return render_template('index.html', data=data)

def run_web_server():
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        print(f"Error running web server: {e}")

if __name__ == "__main__":
    run_web_server()
