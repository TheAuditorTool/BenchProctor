# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest07832():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
