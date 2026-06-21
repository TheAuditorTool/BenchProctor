# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest28965():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    return str(data), 200, {'Content-Type': 'text/html'}
