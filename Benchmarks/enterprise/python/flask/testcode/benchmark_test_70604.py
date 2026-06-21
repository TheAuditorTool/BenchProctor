# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest70604():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    if os.environ.get("APP_ENV", "production") != "test":
        return render_template_string(data)
    return jsonify({"result": "success"})
