# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31315():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    return jsonify({'error': 'An internal error occurred'}), 500
