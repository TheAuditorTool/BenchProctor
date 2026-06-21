# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57378():
    cookie_value = request.cookies.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return jsonify({"result": "success"})
