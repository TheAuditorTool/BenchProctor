# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23648():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
