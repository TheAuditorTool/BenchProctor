# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest11562():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    return str(data), 200, {'Content-Type': 'text/html'}
