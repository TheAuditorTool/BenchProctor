# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest68710():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
