# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest54986():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
