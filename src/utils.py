import re


def format_response(entry):
    return {'data': {'type': 'readings', 'id': entry[0], 'attributes': {'date': entry[1], 'temperature': entry[2], 'pressure': entry[3], 'humidity': entry[4], 'pm25': entry[5]}}}


def validate_date(date):
    if date is None:
        return True
    pattern = re.compile(
        '^([0-9]{4})-(1[0-2]|0[1-9])-(3[0-1]|2[0-9]|1[0-9]|0[1-9])+$')
    return pattern.match(date)


def validate_limit(limit):
    if limit is None:
        return True
    pattern = re.compile('^[0-9]*$')
    return pattern.match(limit)


def validate_data(limit, date_from, date_to):
    if not (validate_date(date_from) and validate_date(date_to) and validate_limit(limit)):
        raise ValueError('Incorrect date format')


def construct_query(limit, date_from, date_to):
    query = 'SELECT * FROM enviro_data'
    from_query = "datetime >= date('%s')" % (date_from)
    to_query = "datetime < date('%s', '+1 day')" % (date_to)

    if date_from and date_to:
        query += ' WHERE ' + from_query + ' AND ' + to_query
    elif date_from:
        query += ' WHERE ' + from_query
    elif date_to:
        query += ' WHERE ' + to_query

    query += ' ORDER BY datetime ASC'

    if limit:
        query += ' LIMIT ' + limit

    return query
