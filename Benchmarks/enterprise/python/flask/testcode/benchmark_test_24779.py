# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest24779():
    raw_body = request.get_data(as_text=True)
    data = default_blank(raw_body)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
