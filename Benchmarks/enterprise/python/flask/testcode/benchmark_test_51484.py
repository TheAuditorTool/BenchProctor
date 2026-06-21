# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request


def BenchmarkTest51484():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    return str(data), 200, {'Content-Type': 'text/html'}
