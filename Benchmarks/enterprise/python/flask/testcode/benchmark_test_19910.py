# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest19910():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
