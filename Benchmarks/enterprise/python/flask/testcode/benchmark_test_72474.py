# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest72474():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
