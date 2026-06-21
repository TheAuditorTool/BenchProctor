# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest12964():
    auth_header = request.headers.get('Authorization', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
