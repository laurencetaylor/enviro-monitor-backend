import flask
from flask import request
import db
import json
from datetime import timedelta

from utils import construct_query, format_response

app = flask.Flask(__name__)
app.config['DEBUG'] = True


def get_readings(limit, date_from, date_to):
    query = construct_query(limit, date_from, date_to)

    try:
        data = db.get_readings(query)
    except:
        return json.dumps({'status': 500, 'title': 'Internal Error', 'message': 'Something went wrong'}), 500, {'ContentType': 'application/json'}

    result = list(map(format_response, data))
    return json.dumps(result), 200, {'ContentType': 'application/json'}


@app.route('/readings', methods=['GET'])
def home():
    limit = request.args.get('limit')
    date_from = request.args.get('dateFrom')
    date_to = request.args.get('dateTo')
    return get_readings(limit, date_from, date_to)


app.run()
