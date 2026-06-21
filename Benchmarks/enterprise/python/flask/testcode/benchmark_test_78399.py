# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import json
from flask import request, jsonify


def BenchmarkTest78399():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
