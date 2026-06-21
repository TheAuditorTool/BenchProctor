# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54634():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    return jsonify({'error': 'An internal error occurred'}), 500
