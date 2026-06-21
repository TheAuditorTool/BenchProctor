# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
import json


def BenchmarkTest55734():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
