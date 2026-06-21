# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest31128():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    return str(data), 200, {'Content-Type': 'text/html'}
