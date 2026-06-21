# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest03298():
    auth_header = request.headers.get('Authorization', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
