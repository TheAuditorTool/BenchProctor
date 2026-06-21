# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest10925():
    upload_name = request.files['upload'].filename
    data = handle(upload_name)
    os.remove(str(data))
    return jsonify({"result": "success"})
