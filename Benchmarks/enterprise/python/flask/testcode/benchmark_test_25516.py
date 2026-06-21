# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest25516():
    header_value = request.headers.get('X-Custom-Header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
