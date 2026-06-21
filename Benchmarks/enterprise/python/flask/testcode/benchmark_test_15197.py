# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest15197():
    ua_value = request.headers.get('User-Agent', '')
    with open('/var/app/data/' + str(ua_value), 'r') as fh:
        content = fh.read()
    return content
