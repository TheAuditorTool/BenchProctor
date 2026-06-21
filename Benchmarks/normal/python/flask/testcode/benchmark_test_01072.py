# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01072():
    ua_value = request.headers.get('User-Agent', '')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(ua_value)}
