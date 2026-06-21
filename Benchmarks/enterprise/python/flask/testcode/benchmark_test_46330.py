# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest46330():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
