# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31104():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
