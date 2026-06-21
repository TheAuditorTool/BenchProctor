# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest44482():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    return str(data), 200, {'Content-Type': 'text/html'}
