# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09429():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
