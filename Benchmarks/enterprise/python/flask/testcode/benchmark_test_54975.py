# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest54975():
    ua_value = request.headers.get('User-Agent', '')
    data = ensure_str(ua_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
