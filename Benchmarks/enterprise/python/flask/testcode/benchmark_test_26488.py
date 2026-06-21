# SPDX-License-Identifier: Apache-2.0
import html
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest26488():
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    processed = str(data).replace("<script", "")
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
