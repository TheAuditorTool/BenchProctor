# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest18014():
    auth_header = request.headers.get('Authorization', '')
    data = to_text(auth_header)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
