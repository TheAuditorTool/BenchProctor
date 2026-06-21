# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08287():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
