# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest41374():
    cookie_value = request.cookies.get('session_token', '')
    with open('/var/app/data/' + str(cookie_value), 'r') as fh:
        content = fh.read()
    return content
