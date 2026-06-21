# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest35169():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(json_value), max_age=86400)
    return resp
