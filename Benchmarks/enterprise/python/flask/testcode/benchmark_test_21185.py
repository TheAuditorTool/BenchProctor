# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21185():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
