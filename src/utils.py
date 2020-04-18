def format_response(entry):
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
