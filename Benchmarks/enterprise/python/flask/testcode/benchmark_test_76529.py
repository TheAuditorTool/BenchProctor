# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest76529():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    return str(data), 200, {'Content-Type': 'text/html'}
