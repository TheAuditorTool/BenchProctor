# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01454():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
