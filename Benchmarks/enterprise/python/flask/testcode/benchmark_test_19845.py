# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19845():
    ua_value = request.headers.get('User-Agent', '')
    return jsonify({'error': str(ua_value), 'stack': repr(locals())}), 500
