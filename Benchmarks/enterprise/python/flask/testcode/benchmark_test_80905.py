# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest80905():
    ua_value = request.headers.get('User-Agent', '')
    data = handle(ua_value)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
