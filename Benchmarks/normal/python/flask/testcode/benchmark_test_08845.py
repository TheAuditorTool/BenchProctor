# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest08845():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
