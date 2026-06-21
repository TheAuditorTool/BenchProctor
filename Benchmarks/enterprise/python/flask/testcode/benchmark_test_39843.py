# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest39843():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    return str(data), 200, {'Content-Type': 'text/html'}
