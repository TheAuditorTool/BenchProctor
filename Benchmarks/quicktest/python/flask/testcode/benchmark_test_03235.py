# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest03235():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
