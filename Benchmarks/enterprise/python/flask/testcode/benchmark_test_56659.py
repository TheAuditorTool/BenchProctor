# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest56659():
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
