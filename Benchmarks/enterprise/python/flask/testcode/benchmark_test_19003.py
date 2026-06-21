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

def BenchmarkTest19003():
    xml_value = request.get_data(as_text=True)
    data = handle(xml_value)
    def _primary():
        return render_template_string(data)
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
