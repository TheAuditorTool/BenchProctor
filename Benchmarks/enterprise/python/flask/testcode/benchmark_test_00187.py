# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00187():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
