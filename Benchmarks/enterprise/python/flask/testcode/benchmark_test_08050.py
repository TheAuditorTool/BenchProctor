# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08050():
    ua_value = request.headers.get('User-Agent', '')
    return jsonify({'error': 'An internal error occurred'}), 500
