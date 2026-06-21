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

def BenchmarkTest52982():
    host_value = request.headers.get('Host', '')
    data = handle(host_value)
    def _primary():
        return Markup('<img src="' + str(data) + '">')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
