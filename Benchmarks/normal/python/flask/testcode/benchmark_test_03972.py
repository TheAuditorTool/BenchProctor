# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest03972():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    return str(data), 200, {'Content-Type': 'text/html'}
