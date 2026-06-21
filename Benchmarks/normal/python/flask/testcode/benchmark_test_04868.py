# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04868():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    return jsonify({'error': 'An internal error occurred'}), 500
