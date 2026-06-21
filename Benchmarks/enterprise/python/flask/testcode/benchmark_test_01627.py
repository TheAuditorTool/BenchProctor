# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01627():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
