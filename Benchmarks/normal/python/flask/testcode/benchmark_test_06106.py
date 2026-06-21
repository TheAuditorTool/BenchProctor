# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06106():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
