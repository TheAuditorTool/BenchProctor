# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest40815():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
