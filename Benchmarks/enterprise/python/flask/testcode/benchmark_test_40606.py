# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40606():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    return jsonify({'error': 'An internal error occurred'}), 500
