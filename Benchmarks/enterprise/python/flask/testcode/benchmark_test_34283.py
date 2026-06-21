# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest34283():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
