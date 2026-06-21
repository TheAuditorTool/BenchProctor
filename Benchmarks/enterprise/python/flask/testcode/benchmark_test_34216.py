# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest34216():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
