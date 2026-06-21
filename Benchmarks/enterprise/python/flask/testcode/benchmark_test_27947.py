# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27947():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    return jsonify({'error': 'An internal error occurred'}), 500
