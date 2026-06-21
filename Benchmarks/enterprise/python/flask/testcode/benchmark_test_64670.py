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

def BenchmarkTest64670():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = handle(forwarded_ip)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
