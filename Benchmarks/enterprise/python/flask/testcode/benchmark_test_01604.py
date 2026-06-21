# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest01604():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    return str(data), 200, {'Content-Type': 'text/html'}
