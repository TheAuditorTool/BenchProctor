# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest66333():
    origin_value = request.headers.get('Origin', '')
    data = ensure_str(origin_value)
    return jsonify({'error': 'An internal error occurred'}), 500
