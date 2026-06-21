# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest32530():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
