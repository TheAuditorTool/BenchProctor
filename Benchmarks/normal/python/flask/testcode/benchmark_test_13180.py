# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13180():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    return jsonify({'error': 'An internal error occurred'}), 500
