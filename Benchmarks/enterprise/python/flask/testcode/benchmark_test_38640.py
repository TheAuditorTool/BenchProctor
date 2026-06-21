# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
import json


def BenchmarkTest38640():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
