# SPDX-License-Identifier: Apache-2.0
from flask import request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest65430():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = handle(json_value)
    def _primary():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
