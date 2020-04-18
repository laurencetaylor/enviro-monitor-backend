import flask
from flask import request
import db
import json
from datetime import timedelta

app = flask.Flask(__name__)
app.config['DEBUG'] = True


def format(entry):
    return {'data': {'type': 'readings', 'id': entry[0], 'attributes': {'date': entry[1], 'temperature': entry[2], 'pressure': entry[3], 'humidity': entry[4], 'pm25': entry[5]}}}


def construct_query(limit, date_from, date_to):
    query = "SELECT * FROM enviro_data"
    from_query = "datetime >= date('%s')" % (date_from)
    to_query = "datetime < date('%s', '+1 day')" % (date_to)

    if date_from and date_to:
        query += " WHERE " + from_query + ' AND ' + to_query
    elif date_from:
        query += " WHERE " + from_query
    elif date_to:
        query += " WHERE " + to_query

    query += ' ORDER BY datetime ASC'

    if limit:
        query += " LIMIT " + limit

    return query


def get_readings(limit, date_from, date_to):
    query = construct_query(limit, date_from, date_to)

    try:
        data = db.get_readings(query)
        result = list(map(format, data))
        return json.dumps(result), 200, {'ContentType': 'application/json'}
    except:
        return json.dumps({'status': 500, 'title': 'Internal Error', 'message': 'Something went wrong'}), 500, {'ContentType': 'application/json'}


@app.route('/readings', methods=['GET'])
def home():
    limit = request.args.get('limit')
    date_from = request.args.get('dateFrom')
    date_to = request.args.get('dateTo')
    return get_readings(limit, date_from, date_to)


app.run()
