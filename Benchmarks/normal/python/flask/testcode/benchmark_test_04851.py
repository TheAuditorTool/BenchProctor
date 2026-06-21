# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest04851():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ensure_str(header_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
