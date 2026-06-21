# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80252():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
