# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest11327():
    header_value = request.headers.get('X-Custom-Header', '')
    with open('/var/app/data/' + str(header_value), 'r') as fh:
        content = fh.read()
    return content
