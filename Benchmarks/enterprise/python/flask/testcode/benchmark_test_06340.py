# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest06340():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
