# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20665():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    return jsonify({'error': 'An internal error occurred'}), 500
