# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01616():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
