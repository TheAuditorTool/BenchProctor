# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request


def BenchmarkTest02315():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
