# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32384():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
