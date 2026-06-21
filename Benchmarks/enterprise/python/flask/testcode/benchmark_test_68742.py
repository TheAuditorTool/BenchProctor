# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68742():
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
