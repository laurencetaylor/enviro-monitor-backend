import flask
import db

app = flask.Flask(__name__)
app.config['DEBUG'] = True


def to_obj(entry):
    return {'data': {'type': 'readings', 'id': entry[0], 'attributes': {'date': entry[1], 'temperature': entry[2], 'pressure': entry[3], 'humidity': entry[4], 'pm25': entry[5]}}}


def readings_get():
    data = db.get_readings()
    transformed_data = list(map(to_obj, data))
    return flask.jsonify(transformed_data)


@app.route('/readings', methods=['GET'])
def home():
    return readings_get()


app.run()
