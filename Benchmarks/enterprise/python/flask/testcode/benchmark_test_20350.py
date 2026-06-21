# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest20350():
    auth_header = request.headers.get('Authorization', '')
    with open('/var/app/data/' + str(auth_header), 'r') as fh:
        content = fh.read()
    return content
