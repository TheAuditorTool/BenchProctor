# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request


def BenchmarkTest20714():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
