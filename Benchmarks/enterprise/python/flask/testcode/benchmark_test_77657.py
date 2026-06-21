# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77657():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
