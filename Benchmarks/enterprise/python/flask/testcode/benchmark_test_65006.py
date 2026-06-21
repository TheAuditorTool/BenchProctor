# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65006():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
