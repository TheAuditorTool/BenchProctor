# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest02198():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = to_text(forwarded_ip)
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
