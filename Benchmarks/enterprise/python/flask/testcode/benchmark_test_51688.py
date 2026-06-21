# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest51688():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
