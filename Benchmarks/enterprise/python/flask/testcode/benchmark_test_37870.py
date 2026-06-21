# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest37870():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
