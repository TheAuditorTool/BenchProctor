# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest03363():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
