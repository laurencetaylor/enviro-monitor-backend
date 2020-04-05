import flask
import db

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return f"""{db.get_readings()}"""


app.run()