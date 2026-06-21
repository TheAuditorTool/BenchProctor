# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest81037():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    auth_check('user', data)
    return jsonify({"result": "success"})
