# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65760():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    return jsonify({'error': 'An internal error occurred'}), 500
