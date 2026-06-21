# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53196():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
