# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import json
from flask import request, jsonify


def BenchmarkTest67534():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
