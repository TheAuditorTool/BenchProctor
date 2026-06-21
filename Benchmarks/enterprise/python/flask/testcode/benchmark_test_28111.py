# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest28111():
    origin_value = request.headers.get('Origin', '')
    return '<html><body><h1>' + str(origin_value) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
