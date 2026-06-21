# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request, jsonify
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest50792():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    if time.time() > 1000000000:
        return redirect(str(data))
    return jsonify({"result": "success"})
