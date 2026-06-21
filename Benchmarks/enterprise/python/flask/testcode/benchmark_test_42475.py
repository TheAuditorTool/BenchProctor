# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42475():
    cookie_value = request.cookies.get('session_token', '')
    globals().setdefault('_secret_cache', {})['current'] = str(cookie_value)
    return jsonify({"result": "success"})
