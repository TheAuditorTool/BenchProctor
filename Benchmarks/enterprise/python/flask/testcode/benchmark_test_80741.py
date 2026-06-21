# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest80741():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
