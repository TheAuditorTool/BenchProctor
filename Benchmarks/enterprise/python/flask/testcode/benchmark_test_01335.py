# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest01335():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
