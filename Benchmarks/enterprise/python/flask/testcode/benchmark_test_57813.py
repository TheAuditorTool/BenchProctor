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

def BenchmarkTest57813():
    user_id = request.args.get('id', '')
    data = handle(user_id)
    def _primary():
        return Markup('<div>' + str(data) + '</div>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
