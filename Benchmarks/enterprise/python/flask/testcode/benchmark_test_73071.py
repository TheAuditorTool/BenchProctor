# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73071():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    return jsonify({'error': 'An internal error occurred'}), 500
