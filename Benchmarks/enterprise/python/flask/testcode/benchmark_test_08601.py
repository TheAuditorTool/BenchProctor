# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest08601():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
