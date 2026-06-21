# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest62582():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    return str(data), 200, {'Content-Type': 'text/html'}
