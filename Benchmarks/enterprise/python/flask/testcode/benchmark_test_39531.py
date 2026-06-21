# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39531():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
