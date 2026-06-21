# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest20256():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
