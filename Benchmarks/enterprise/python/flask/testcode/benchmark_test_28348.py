# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28348():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    return jsonify({'error': 'An internal error occurred'}), 500
