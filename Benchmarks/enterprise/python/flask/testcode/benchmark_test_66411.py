# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66411():
    origin_value = request.headers.get('Origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    return jsonify({'error': 'An internal error occurred'}), 500
