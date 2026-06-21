# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24813():
    cookie_value = request.cookies.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
