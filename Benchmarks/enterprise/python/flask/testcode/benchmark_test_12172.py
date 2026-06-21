# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest12172():
    header_value = request.headers.get('X-Custom-Header', '')
    data = handle(header_value)
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
