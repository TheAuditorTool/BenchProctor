# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import session
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest08963():
    field_value = request.form.get('field', '')
    data = default_blank(field_value)
    session.clear()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
