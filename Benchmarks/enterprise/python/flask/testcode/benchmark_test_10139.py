# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10139():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    return jsonify({'error': 'An internal error occurred'}), 500
