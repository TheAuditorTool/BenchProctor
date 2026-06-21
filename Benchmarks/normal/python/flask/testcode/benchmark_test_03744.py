# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest03744():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
