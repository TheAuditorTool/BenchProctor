# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest49389():
    host_value = request.headers.get('Host', '')
    data = ensure_str(host_value)
    return jsonify({'error': 'An internal error occurred'}), 500
