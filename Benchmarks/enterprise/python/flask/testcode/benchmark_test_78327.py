# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78327():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
