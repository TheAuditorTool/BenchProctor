# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest23655():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ensure_str(header_value)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
