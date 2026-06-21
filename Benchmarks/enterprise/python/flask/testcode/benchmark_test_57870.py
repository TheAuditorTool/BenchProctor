# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57870():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    return jsonify({'error': 'An internal error occurred'}), 500
