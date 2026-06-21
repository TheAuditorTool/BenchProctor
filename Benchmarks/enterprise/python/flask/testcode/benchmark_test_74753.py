# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74753():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
