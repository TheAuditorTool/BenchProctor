# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest38578():
    auth_header = request.headers.get('Authorization', '')
    data = relay_value(auth_header)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
