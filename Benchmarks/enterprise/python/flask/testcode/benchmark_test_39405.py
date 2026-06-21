# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest39405():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
