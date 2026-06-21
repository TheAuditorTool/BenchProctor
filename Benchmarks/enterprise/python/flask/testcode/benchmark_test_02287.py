# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest02287():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
