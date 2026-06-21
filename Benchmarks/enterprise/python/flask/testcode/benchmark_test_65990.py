# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest65990():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    processed = data[:64]
    return render_template_string(processed)
