# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest78682():
    ua_value = request.headers.get('User-Agent', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return str(data), 200, {'Content-Type': 'text/html'}
