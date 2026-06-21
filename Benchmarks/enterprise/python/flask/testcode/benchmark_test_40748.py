# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
from flask import session


def to_text(value):
    return str(value).strip()

def BenchmarkTest40748():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = to_text(json_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
