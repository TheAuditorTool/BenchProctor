# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest13052():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
