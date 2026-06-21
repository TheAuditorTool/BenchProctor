# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest05944():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = relay_value(json_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
