# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58344():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    return jsonify({'error': 'An internal error occurred'}), 500
