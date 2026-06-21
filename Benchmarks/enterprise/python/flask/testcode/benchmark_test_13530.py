# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest13530(path_param):
    path_value = path_param
    data = handle(path_value)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
