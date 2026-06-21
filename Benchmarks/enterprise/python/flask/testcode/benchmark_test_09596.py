# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09596():
    origin_value = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
