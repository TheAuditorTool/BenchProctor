# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest47879():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    return str(data), 200, {'Content-Type': 'text/html'}
