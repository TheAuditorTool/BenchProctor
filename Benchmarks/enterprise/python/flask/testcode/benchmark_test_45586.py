# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest45586():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = relay_value(json_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
