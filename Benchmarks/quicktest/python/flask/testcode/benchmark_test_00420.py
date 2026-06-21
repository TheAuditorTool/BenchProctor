# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from flask import render_template_string


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest00420():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    return render_template_string('{{ value }}', value=data)
