# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest51913():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    return str(data), 200, {'Content-Type': 'text/html'}
