# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05381():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
