# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest12919():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
