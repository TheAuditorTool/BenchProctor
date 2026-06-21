# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest06442():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
