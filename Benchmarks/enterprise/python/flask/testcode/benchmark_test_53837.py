# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest53837():
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
