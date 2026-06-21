# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest43035():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    return str(data), 200, {'Content-Type': 'text/html'}
