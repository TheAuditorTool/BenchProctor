# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41280():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
