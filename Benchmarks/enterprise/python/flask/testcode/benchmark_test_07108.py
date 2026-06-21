# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07108():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
