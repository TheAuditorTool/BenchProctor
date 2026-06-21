# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45277():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
