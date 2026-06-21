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

def BenchmarkTest21398():
    field_value = request.form.get('field', '')
    data = handle(field_value)
    processed = re.sub(r'\d+', '****', str(data))
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
