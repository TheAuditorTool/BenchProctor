# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest30259():
    ua_value = request.headers.get('User-Agent', '')
    data = handle(ua_value)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
