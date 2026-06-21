# SPDX-License-Identifier: Apache-2.0
from flask import request


def ensure_str(value):
    return str(value)

def BenchmarkTest28227():
    raw_body = request.get_data(as_text=True)
    data = ensure_str(raw_body)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
