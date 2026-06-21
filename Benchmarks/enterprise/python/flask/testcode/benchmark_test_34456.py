# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import json


def BenchmarkTest34456():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    session['data'] = str(data)
    return jsonify({"result": "success"})
