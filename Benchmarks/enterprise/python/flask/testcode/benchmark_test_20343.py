# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest20343():
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
