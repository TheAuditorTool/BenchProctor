# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import tempfile


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest06994():
    ua_value = request.headers.get('User-Agent', '')
    data = handle(ua_value)
    checked_path = os.path.normpath(data)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(checked_path))
    return jsonify({"result": "success"})
