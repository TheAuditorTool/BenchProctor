# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest60725():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
