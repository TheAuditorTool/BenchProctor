# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest04291():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
