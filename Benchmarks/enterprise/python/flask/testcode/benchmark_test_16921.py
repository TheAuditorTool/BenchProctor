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

def BenchmarkTest16921():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = handle(forwarded_ip)
    processed = data[:64]
    return Markup('<div>' + str(processed) + '</div>')
