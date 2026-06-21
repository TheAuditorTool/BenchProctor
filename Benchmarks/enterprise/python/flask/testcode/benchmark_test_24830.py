# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24830():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
