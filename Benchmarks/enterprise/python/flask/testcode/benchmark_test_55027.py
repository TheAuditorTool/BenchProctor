# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55027():
    host_value = request.headers.get('Host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
