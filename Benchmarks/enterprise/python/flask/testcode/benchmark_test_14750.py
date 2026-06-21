# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest14750():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = to_text(json_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
