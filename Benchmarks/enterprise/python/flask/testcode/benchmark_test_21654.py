# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import json


def BenchmarkTest21654():
    origin_value = request.headers.get('Origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    session['data'] = str(data)
    return jsonify({"result": "success"})
