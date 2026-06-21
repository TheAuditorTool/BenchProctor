# SPDX-License-Identifier: Apache-2.0
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest43103():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    return str(data), 200, {'Content-Type': 'text/html'}
