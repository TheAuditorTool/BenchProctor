# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06645():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    return jsonify({'error': 'An internal error occurred'}), 500
