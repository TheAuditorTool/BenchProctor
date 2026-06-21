# SPDX-License-Identifier: Apache-2.0


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest46179(path_param):
    path_value = path_param
    data = handle(path_value)
    return str(data), 200, {'Content-Type': 'text/html'}
