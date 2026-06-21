# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest26470():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
