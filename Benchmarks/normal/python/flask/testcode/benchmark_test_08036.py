# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest08036():
    ua_value = request.headers.get('User-Agent', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
