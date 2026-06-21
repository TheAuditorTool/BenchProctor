# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest00491():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
