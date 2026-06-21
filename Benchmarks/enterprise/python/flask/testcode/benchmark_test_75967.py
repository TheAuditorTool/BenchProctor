# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest75967():
    host_value = request.headers.get('Host', '')
    data = handle(host_value)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
