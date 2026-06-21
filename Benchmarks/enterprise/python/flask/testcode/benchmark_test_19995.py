# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest19995():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
