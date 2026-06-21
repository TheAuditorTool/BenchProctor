# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import os


def BenchmarkTest43727():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
