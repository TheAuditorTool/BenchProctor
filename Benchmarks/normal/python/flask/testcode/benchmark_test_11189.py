# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11189():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500
