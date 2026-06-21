# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53242():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
