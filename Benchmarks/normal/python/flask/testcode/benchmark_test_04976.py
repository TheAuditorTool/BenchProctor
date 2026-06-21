# SPDX-License-Identifier: Apache-2.0
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest04976():
    header_value = request.headers.get('X-Custom-Header', '')
    data = to_text(header_value)
    return str(data), 200, {'Content-Type': 'text/html'}
