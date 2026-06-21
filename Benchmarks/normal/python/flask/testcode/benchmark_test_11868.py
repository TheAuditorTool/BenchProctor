# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import json


def BenchmarkTest11868():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
