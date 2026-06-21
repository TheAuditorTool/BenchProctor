# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest16451():
    ua_value = request.headers.get('User-Agent', '')
    data = str(ua_value).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
