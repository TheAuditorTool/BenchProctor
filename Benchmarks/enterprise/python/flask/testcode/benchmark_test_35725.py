# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest35725():
    auth_header = request.headers.get('Authorization', '')
    data = coalesce_blank(auth_header)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
