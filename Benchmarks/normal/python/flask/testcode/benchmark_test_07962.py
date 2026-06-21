# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07962():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
