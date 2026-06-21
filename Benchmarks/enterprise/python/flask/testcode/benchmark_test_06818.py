# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest06818():
    multipart_value = request.form.get('multipart_field', '')
    data = to_text(multipart_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
