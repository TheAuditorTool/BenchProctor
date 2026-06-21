# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78612():
    cookie_value = request.cookies.get('session_token', '')
    return jsonify({'error': str(cookie_value), 'stack': repr(locals())}), 500
