# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest48103():
    ua_value = request.headers.get('User-Agent', '')
    data = handle(ua_value)
    return render_template_string('safe block: {{ value }}', value=data)
