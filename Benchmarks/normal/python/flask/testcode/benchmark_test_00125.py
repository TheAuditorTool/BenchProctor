# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest00125():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = default_blank(forwarded_ip)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
