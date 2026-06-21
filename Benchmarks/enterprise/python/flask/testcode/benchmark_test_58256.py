# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest58256():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
