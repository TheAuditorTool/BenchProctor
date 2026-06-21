# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest65270():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
