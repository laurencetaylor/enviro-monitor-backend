import flask
import db

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def to_obj(entry):
    return {'date': entry[1], 'temperature': entry[2], 'pressure': entry[3], 'humidity': entry[4], 'pm25': entry[5]}

def to_json(data):
    new_data = list(map(to_obj, data))
    return flask.jsonify(new_data)

@app.route('/', methods=['GET'])
def home():
    readings = db.get_readings()
    return to_json(readings)


app.run()