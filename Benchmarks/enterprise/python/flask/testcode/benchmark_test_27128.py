# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest27128():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
