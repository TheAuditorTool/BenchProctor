# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import re
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest18191():
    auth_header = request.headers.get('Authorization', '')
    data = handle(auth_header)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
