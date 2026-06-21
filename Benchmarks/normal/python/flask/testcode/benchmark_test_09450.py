# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import json


def BenchmarkTest09450():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
