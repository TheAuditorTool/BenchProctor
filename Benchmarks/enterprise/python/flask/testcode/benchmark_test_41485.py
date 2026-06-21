# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest41485():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
