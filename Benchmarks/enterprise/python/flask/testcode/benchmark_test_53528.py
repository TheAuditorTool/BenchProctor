# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest53528():
    raw_body = request.get_data(as_text=True)
    data = to_text(raw_body)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
