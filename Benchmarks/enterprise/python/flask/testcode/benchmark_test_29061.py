# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest29061():
    origin_value = request.headers.get('Origin', '')
    data = ensure_str(origin_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
