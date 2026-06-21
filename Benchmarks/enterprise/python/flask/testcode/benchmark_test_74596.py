# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest74596():
    host_value = request.headers.get('Host', '')
    data = relay_value(host_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
