# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest14076():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
