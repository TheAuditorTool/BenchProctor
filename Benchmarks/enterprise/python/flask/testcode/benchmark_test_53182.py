# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53182():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
