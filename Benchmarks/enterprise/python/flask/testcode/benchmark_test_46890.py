# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest46890():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    return str(data), 200, {'Content-Type': 'text/html'}
