# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42745():
    ua_value = request.headers.get('User-Agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
