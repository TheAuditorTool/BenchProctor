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

def BenchmarkTest04323():
    referer_value = request.headers.get('Referer', '')
    data = handle(referer_value)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
