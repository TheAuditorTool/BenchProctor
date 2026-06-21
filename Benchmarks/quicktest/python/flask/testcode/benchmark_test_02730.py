# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest02730():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
