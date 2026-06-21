# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest35313():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
