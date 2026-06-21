# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest03012():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
