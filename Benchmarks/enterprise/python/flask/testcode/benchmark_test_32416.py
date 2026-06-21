# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest32416():
    host_value = request.headers.get('Host', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return str(data), 200, {'Content-Type': 'text/html'}
