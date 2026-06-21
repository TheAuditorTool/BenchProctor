# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest10130():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
