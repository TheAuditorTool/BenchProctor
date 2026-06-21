# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest13287():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
