# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06319():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
