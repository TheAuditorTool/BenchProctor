# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest40897():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
