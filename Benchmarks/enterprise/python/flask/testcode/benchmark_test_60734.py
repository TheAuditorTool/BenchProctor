# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest60734():
    header_value = request.headers.get('X-Custom-Header', '')
    data = handle(header_value)
    def _primary():
        return Markup('<div>' + str(data) + '</div>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
