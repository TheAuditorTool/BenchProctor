# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest75943():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
