# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63746():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
