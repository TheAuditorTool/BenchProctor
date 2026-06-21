# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75108():
    ua_value = request.headers.get('User-Agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
