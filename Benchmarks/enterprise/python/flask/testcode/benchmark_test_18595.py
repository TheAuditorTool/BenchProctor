# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18595():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
