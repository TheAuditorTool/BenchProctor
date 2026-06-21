# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04123():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
