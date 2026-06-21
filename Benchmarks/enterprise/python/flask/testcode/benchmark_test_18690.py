# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18690():
    origin_value = request.headers.get('Origin', '')
    return jsonify({'error': 'An internal error occurred'}), 500
