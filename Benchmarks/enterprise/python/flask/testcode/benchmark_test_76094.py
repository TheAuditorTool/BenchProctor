# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76094():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
