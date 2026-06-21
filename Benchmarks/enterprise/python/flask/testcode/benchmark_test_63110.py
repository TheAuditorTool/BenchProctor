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

def BenchmarkTest63110():
    upload_name = request.files['upload'].filename
    data = handle(upload_name)
    def _primary():
        return render_template_string(data)
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
