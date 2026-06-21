# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00416():
    host_value = request.headers.get('Host', '')
    data = '{}'.format(host_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
