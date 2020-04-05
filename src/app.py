# import flask

# app = flask.Flask(__name__)
# app.config["DEBUG"] = True


# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


# app.run()

import db
import sensor

db.create_table()
data = sensor.get_readings()
db.insert_readings(data["temperature"], data["pressure"],
                   data["humidity"], data["pm25"])

print(db.get_readings())
