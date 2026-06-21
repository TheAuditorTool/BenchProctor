# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49275():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
