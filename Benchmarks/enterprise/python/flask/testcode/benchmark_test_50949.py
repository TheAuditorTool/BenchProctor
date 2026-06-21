# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest50949():
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
