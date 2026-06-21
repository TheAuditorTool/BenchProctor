# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest81431():
    xml_value = request.get_data(as_text=True)
    data = handle(xml_value)
    processed = data[:64]
    return redirect(str(processed))
