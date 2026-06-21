# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest35408():
    header_value = request.headers.get('X-Custom-Header', '')
    data = to_text(header_value)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
