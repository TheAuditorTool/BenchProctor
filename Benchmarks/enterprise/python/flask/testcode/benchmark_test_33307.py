# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33307():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
