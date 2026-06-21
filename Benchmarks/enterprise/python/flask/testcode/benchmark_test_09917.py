# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest09917():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    return str(data), 200, {'Content-Type': 'text/html'}
