# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest27383():
    auth_header = request.headers.get('Authorization', '')
    data = default_blank(auth_header)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
