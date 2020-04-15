import flask
from flask import request
import db
import json

app = flask.Flask(__name__)
app.config['DEBUG'] = True


def to_obj(entry):
    return {'data': {'type': 'readings', 'id': entry[0], 'attributes': {'date': entry[1], 'temperature': entry[2], 'pressure': entry[3], 'humidity': entry[4], 'pm25': entry[5]}}}


def readings_get(limit):
    data = db.get_readings(limit)
    return list(map(to_obj, data))


@app.route('/readings', methods=['GET'])
def home():
    limit = request.args.get('limit')

    try:
        return json.dumps(readings_get(limit)), 200, {'ContentType': 'application/json'}
    except:
        return json.dumps({'status': 500, 'error': 'Internal Error'}), 500, {'ContentType': 'application/json'}


app.run()
