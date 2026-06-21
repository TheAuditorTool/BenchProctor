# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest60492():
    header_value = request.headers.get('X-Custom-Header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    return str(data), 200, {'Content-Type': 'text/html'}
