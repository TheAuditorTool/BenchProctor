# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest38077():
    origin_value = request.headers.get('Origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
