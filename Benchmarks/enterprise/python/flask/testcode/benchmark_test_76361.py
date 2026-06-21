# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest76361():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
