# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33963():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
