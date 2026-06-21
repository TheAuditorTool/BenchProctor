# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest15721():
    header_value = request.headers.get('X-Custom-Header', '')
    data = handle(header_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
