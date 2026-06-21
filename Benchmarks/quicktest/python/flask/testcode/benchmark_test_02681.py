# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest02681():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
