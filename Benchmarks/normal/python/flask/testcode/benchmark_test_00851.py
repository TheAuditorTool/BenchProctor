# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest00851():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
