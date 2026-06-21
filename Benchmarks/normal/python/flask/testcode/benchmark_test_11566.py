# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest11566():
    origin_value = request.headers.get('Origin', '')
    data = relay_value(origin_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
