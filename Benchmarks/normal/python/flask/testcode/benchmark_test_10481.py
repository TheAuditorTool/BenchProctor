# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest10481():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value}'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
