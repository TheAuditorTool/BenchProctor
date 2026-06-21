# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest03033():
    auth_header = request.headers.get('Authorization', '')
    data = '{}'.format(auth_header)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
