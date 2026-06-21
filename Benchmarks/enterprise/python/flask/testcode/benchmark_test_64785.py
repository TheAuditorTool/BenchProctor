# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest64785():
    auth_header = request.headers.get('Authorization', '')
    data = ensure_str(auth_header)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
