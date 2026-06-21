# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15141():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
