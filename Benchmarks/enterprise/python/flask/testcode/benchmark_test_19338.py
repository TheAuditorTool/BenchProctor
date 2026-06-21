# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest19338():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
