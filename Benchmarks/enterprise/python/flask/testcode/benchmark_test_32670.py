# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import json


def BenchmarkTest32670():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
