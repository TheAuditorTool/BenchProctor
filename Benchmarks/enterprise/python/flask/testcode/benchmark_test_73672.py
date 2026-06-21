# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73672():
    cookie_value = request.cookies.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
