# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10456():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
