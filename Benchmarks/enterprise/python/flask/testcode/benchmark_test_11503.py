# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11503():
    host_value = request.headers.get('Host', '')
    data = '{}'.format(host_value)
    return jsonify({'error': 'An internal error occurred'}), 500
