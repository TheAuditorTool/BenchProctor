# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest08344():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = handle(json_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
