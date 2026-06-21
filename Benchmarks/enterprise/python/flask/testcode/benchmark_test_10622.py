# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest10622():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
