# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44159():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
