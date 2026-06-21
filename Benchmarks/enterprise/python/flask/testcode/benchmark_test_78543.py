# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest78543():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    return str(data), 200, {'Content-Type': 'text/html'}
