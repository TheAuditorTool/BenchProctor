# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest10530():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    return str(data), 200, {'Content-Type': 'text/html'}
