# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest05245():
    raw_body = request.get_data(as_text=True)
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    return str(data), 200, {'Content-Type': 'text/html'}
