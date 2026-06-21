# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest29521():
    origin_value = request.headers.get('Origin', '')
    data = coalesce_blank(origin_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
