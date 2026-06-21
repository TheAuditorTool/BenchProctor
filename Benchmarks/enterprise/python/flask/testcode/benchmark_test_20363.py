# SPDX-License-Identifier: Apache-2.0
from flask import request


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest20363():
    header_value = request.headers.get('X-Custom-Header', '')
    data = default_blank(header_value)
    return str(data), 200, {'Content-Type': 'text/html'}
