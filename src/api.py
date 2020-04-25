import flask
from flask import request
import db
import json
from flask_cors import CORS

from utils import construct_query, format_response, validate_data

app = flask.Flask(__name__)
app.config['DEBUG'] = True
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})


def get_readings(limit, date_from, date_to):
    try:
        validate_data(limit, date_from, date_to)
    except:
        return json.dumps({'status': 400, 'title': 'Bad Request Error', 'message': 'Invalid parameters'}), 400, {'ContentType': 'application/json'}

    query = construct_query(limit, date_from, date_to)

    try:
        data = db.get_readings(query)
    except:
        return json.dumps({'status': 500, 'title': 'Internal Error', 'message': 'Problem with the database'}), 500, {'ContentType': 'application/json'}

    result = list(map(format_response, data))
    return json.dumps(result), 200, {'ContentType': 'application/json'}


@app.route('/readings', methods=['GET'])
def home():
    limit = request.args.get('limit')
    date_from = request.args.get('dateFrom')
    date_to = request.args.get('dateTo')
    return get_readings(limit, date_from, date_to)


app.run()
