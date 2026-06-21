# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest61616():
    cookie_value = request.cookies.get('session_token', '')
    return str(cookie_value), 200, {'Content-Type': 'text/html'}
