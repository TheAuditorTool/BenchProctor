# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest67924():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
