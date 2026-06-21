# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest67226():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
