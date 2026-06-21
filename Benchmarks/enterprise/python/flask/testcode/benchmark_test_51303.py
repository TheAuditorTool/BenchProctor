# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest51303():
    auth_header = request.headers.get('Authorization', '')
    data = handle(auth_header)
    processed = str(data).replace("<script", "")
    return Markup('<div>' + str(processed) + '</div>')
