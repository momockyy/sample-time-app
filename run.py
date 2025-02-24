from flask import Flask, jsonify 
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/time')
def get_time():
    # Get the current time in ISO format
    current_time = datetime.datetime.now().isoformat()
    return jsonify({'time': current_time})


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
