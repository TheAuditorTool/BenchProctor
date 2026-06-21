# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest02606():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
