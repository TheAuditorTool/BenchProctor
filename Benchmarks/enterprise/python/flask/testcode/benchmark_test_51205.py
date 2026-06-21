# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51205():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
