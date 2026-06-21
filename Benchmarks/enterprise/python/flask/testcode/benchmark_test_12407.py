# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest12407():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
