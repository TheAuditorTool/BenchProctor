# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest59939():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
