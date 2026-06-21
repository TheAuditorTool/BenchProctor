# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest00197():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
