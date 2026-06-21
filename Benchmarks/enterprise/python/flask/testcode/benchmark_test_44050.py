# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest44050():
    ua_value = request.headers.get('User-Agent', '')
    data = relay_value(ua_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
