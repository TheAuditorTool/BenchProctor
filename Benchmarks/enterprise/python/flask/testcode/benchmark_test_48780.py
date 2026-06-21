# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest48780():
    header_value = request.headers.get('X-Custom-Header', '')
    data = normalise_input(header_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
