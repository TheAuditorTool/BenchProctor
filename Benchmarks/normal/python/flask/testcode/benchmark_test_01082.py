# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest01082():
    cookie_value = request.cookies.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    json.loads(data)
    return jsonify({"result": "success"})
