# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest58204():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
