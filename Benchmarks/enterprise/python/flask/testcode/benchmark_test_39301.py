# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest39301():
    auth_header = request.headers.get('Authorization', '')
    data = handle(auth_header)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
