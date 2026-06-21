# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67420():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value}'
    return jsonify({'error': 'An internal error occurred'}), 500
