# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest06624():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = handle(forwarded_ip)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
