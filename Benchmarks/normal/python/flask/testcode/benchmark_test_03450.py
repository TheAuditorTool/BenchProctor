# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest03450():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
