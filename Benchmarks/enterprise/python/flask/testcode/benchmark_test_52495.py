# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest52495():
    host_value = request.headers.get('Host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    return str(data), 200, {'Content-Type': 'text/html'}
