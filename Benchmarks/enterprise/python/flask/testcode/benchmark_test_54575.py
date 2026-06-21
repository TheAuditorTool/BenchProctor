# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest54575(path_param):
    path_value = path_param
    data = default_blank(path_value)
    try:
        int(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
