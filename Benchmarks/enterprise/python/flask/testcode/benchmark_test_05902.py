# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest05902():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
