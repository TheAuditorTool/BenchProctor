# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest26722():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    return str(data), 200, {'Content-Type': 'text/html'}
