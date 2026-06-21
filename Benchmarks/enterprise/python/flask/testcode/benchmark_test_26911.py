# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest26911():
    header_value = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
