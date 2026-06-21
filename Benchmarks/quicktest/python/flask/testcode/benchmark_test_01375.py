# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest01375():
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
