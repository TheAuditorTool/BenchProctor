# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05224():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
